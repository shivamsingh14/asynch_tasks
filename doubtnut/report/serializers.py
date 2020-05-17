from rest_framework import serializers

from doubtnut.utils import Config

class ReportSerializer(serializers.BaseSerializer):

	def to_internal_value(self, data):

		if not data:
			error = Config.GENERIC.BAD_REQUEST
			raise serializers.ValidationError({"status": error[0], "message": error[1]})

		if data.get("email_id") == None:
			message = Config.GENERIC.EMAIL_ID_REQUIRED
			raise serializers.ValidationError({"message": message})

		if data.get("similar_questions") == None:
			message = Config.GENERIC.QUESTIONS_LIST
			raise serializers.ValidationError({"message": message})

		return data