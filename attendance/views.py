from django.shortcuts import render, redirect
from . models import Individual, WaitingList, Course
from .forms import IndividualForm, WaitingListForm, CourseForm  # We'll create these forms next

# View to register individuals
def register_individual(request):
    if request.method == 'POST':
        form = IndividualForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_individual')  # Redirect to the same page or another page after registration
    else:
        form = IndividualForm()
    return render(request, 'attendance/register_individual.html', {'form': form})

# View to create a course
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_course')  # Redirect to the same page or another page after course creation
    else:
        form = CourseForm()
    return render(request, 'attendance/create_course.html', {'form': form})
