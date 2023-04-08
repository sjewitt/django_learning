from django.contrib import admin

# Register your models here.

# note import path here, dependent on where the app vs the project are:
from .models import Question

admin.site.register(Question)
