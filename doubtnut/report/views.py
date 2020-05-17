from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.task.control import revoke

from doubtnut.report.tasks import send_mail_task
from doubtnut import utils
from doubtnut.app_logger import AppLogger
from doubtnut.report.serializers import ReportSerializer

from datetime import datetime

logger = AppLogger(tag="Views")

class SummaryAPI(APIView):

    def post(self, request):

        logger.info("Request data: {}".format(request.data))
        s = ReportSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        user_email_id = s.validated_data.get("email_id")
        questions_list = s.validated_data.get("similar_questions")

        countdown = utils.CONSTANTS.CELERY_TIMEOUT

        task_values = utils.RedisUtils.get_cache(user_email_id)
        if (task_values is not None):
            task_values_dict = utils.JsonUtils.convert_to_dict(task_values)
            task_id = task_values_dict['task_id']
            logger.info("revoking task with task id: {}".format(task_id))
            revoke(task_id, terminate=True)
            logger.info("Deleting key: {} with value: {}".format(user_email_id, utils.RedisUtils.get_cache(user_email_id)))
            utils.RedisUtils.delete_cache(user_email_id)

        task_result = send_mail_task.apply_async((str(questions_list), user_email_id), countdown=countdown)
        logger.info("Task's task id: {}".format(task_result.id))
        task_id = task_result.id
        task_data = {"task_id": task_id, "data": questions_list}
        utils.RedisUtils.set_cache_with_ttl(user_email_id, countdown, utils.JsonUtils.convert_to_json(task_data))
    
        response = {"message": "Mail sent successfully"}
        return Response(response, status=status.HTTP_200_OK)
