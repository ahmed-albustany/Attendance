from django import forms
from .models import Individual, WaitingList, course

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['id_type', 'id_number', 'name', 'country', 'phone', 'sex', 'family_id', 'head_of_household']

class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ['name', 'start_date', 'end_date']

class WaitingListForm(forms.ModelForm):
    class Meta:
        model = WaitingList
        fields = ['id_number', 'beneficiary', 'application_sub_category', 'requesting_phone_number']
