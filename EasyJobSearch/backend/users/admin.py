
from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import Certificate
from .models import Experience
from .models import Project
from .models import Job
from .models import Question


admin.site.register(Project)
admin.site.register(UserProfile)
admin.site.register(Certificate)
admin.site.register(Experience)
admin.site.register(Job)
admin.site.register(Question)


