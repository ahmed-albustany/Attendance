from django.contrib import admin
from .models import Individual, WaitingList, Course, UserProfile

admin.site.register(Individual)
admin.site.register(WaitingList)
admin.site.register(Course)
admin.site.register(UserProfile)