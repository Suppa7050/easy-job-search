from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobApplication
from .serializers import JobApplicationSerializer

@api_view(['POST'])
def create_job_application(request):
    if request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new job application
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created data with 201 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

@api_view(['GET'])
def list_job_applications(request):
    if request.method == 'GET':
        job_applications = JobApplication.objects.all()  # Retrieve all job applications
        serializer = JobApplicationSerializer(job_applications, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with 200 status


@api_view(['GET'])
def get_data(request):
    data = {"message": "Hello from Django"}
    return Response(data)
