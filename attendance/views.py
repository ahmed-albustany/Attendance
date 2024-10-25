from pyexpat.errors import messages
from django.shortcuts import render, redirect
from . models import Individual, WaitingList, Course
from .forms import IndividualForm, WaitingListForm, CourseForm  # We'll create these forms next

# View to register individuals
def register_individual(request):
    if request.method == 'POST':
        form = IndividualForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Individual registered successfully.")
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
            return redirect('course_list')  # Redirect to the same page or another page after course creation
    else:
        form = CourseForm()
    return render(request, 'attendance/create_course.html', {'form': form})


# View to handle waiting list submissions
def waiting_list(request):
    if request.method == 'POST':
        form = WaitingListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been added to the waiting list.")
            return redirect('waiting_list')  # Redirect to the same page or another page after submission
    else:
        form = WaitingListForm()
    return render(request, 'attendance/waiting_list_form.html', {'form': form})
