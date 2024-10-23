from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


    def __str__(self):
        return self.title



class JobApplication(models.Model):  # You can name the model whatever you prefer
    name = models.CharField(max_length=100)  # Field for the applicant's name
    applied_job_id = models.IntegerField()     # Field for the applied job ID

    def __str__(self):
        return self.name  # Return the name for better representation in admin
