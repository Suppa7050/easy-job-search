from django.contrib import admin

# Register your models here.
from .models import JobApplication  # Import the new model
from .models import Post

admin.site.register(JobApplication)  # Register the model
admin.site.register(Post)  # Register the model