from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LogSerializer
from .models import Log
from user.models import UsersMan
from datetime import datetime
from dateutil.parser import parse
from django.utils import timezone
from rest_framework import status

# For posting the activity periods of individual members
class LogView(APIView):
    def post(self, request):
        ser = LogSerializer(data = request.data, partial=True)
        if ser.is_valid(raise_exception=True):
            obj = ser.save()
            obj.start_time = datetime.now().strftime('%b %d %Y %I:%M%p')
            print(obj.start_time)
            obj.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Log.objects.all()
        ser = LogSerializer(data, many=True)
        return Response(ser.data)

#for updating the end_time corresponding to each login time
class LogUpdateView(APIView):
    def post(self, request, s_num):
        close = datetime.now().strftime('%b %d %Y %I:%M%p')
        ser = LogSerializer(Log.objects.filter(s_num=s_num).first(), data=request.data, partial=True)
        if ser.is_valid(raise_exception=True):
            obj = ser.save()
            obj.end_time = close
            obj.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
