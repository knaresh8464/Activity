from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ("s_num","s_no", "start_time","end_time")

class LogTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ("start_time", "end_time")