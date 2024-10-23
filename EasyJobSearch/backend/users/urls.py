from django.urls import path
from .views import (
    RegisterView, 
    LoginView,  
    get_user_profile, 
    update_address, 
    delete_user_profile, 
    manage_certificate, 
    manage_experience,
    manage_project,   # New view for managing projects
    manage_education,   # New view for managing education

    #bysuppa
    register_company,
    login_company,
    create_job,
    list_jobs,
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # User Profile management by email
    path('profile/<str:email>/', get_user_profile, name='get_user_profile'),
    path('profile/delete/<str:email>/', delete_user_profile, name='delete_user_profile'),

    
    path('address/manage/<str:email>/', update_address, name='update_user_profile'),
    

    # Certificate management by email
    path('certificate/manage/<str:email>/', manage_certificate, name='manage_certificate'),

    # Experience management by email
    path('experience/manage/<str:email>/', manage_experience, name='manage_experience'),

    # Project management by email
    path('project/manage/<str:email>/', manage_project, name='manage_project'),

    # Education management by email
    path('education/manage/<str:email>/', manage_education, name='manage_education'),


    #by suppa


    path('register_company/', register_company, name='register_company'),
    path('login_company/', login_company, name='login_company'),
    path('create_job/', create_job, name='create_job'),
    path('list_jobs/', list_jobs, name='list_jobs'),
]
