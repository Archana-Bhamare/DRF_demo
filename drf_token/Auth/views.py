from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf_project.Auth import permissions
from drf_project.Auth.models import Student
from drf_project.Auth.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
