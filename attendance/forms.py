from django import forms
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
