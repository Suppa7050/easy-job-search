from django.urls import path
from .views import get_data
from .views import create_job_application,list_job_applications


urlpatterns = [
    path('api/', get_data),
    path('api/job-applications/', create_job_application, name='create_job_application'),
    path('api/job-applications/list/', list_job_applications, name='list_job_applications'),  # New endpoint
]

