from django.contrib import admin
from .models import Individual, WaitingList, Course
# Register your models here.


admin.site.register(Individual)
admin.site.register(WaitingList)
admin.site.register(Course)