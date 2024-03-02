from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from restAPI.drfapp.serializers import StudentSerializer
from .models import Student

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'years_active': 10,
        }
        return Response(data)