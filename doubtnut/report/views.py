from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from celery.task.control import revoke

from doubtnut.report.tasks import task1, task2

from datetime import datetime

class TestView(APIView):

    def post(self, request):

        r = task1.apply_async((1, 4), task_id="user_id_1_question_id_2", countdown=60)
        r1 = task2.apply_async((1, 4), task_id="user_id_1_question_id_3")
        revoke("user_id_1_question_id_2", terminate=True)
        print ("aaaaaaa")
        print (r)
        print (r.ready())
        print (r.get())
        return Response("hieeeee", status=status.HTTP_200_OK)
