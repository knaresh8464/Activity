from rest_framework import serializers
from .models import UsersMan
from log.serializers import LogSerializer, LogTimeSerializer
from log.models import Log
from django.http import HttpResponse
from django.forms.models import model_to_dict

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersMan
        fields = ("s_no","user_id","name","time_zone")

class UserLogSerializer(serializers.ModelSerializer):
    activity_periods = LogTimeSerializer(read_only=True,many=True)

    class Meta:
        model = UsersMan
        depth = 1
        fields = ( "user_id", "name", "time_zone", "activity_periods")

    # def get_activity_periods(self, *args, **kwargs):
    #     x = model_to_dict(Log.objects.all())
    #     print(x)
    #     return HttpResponse(x)

