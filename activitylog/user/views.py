from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserLogSerializer
from .models import UsersMan
from rest_framework import status
from django.db.models import F

#For posting the information about users and saving it in db and getting the information about all users from db
class UsersView(APIView):
    def post(self, request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        data = UsersMan.objects.values(
            'user_id',
            'name',
            'time_zone'
        )
        ser = UserSerializer(data, many=True)
        return Response(ser.data)
        
#for displaying the final result.
class MembersActivity(APIView):
    def get(self, request):
        data = UsersMan.objects.all()
        ser = UserLogSerializer(data, many=True)
        return Response(ser.data)