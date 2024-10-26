from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Individual, WaitingList, Course


    

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['id_type', 'id_number', 'name', 'country', 'phone', 'sex', 'family_id', 'head_of_household']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'age_range', 'start_date', 'end_date', 'description']


class WaitingListForm(forms.ModelForm):
    class Meta:
        model = WaitingList
        fields = ['id_number', 'beneficiary', 'sub_category', 'phone_number']




# # for user registration
# class UserRegistrationForm(UserCreationForm):
#     program = forms.CharField(max_length=100)

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'program']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.save()  # Save the User model first
#         user_profile = UserProfile(user=user, program=self.cleaned_data['program'])
#         if commit:
#             user_profile.save()  # Save the UserProfile model next
#         return user
