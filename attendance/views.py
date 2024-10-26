from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from . models import Individual, WaitingList, Course
from .forms import IndividualForm, WaitingListForm, CourseForm  # We'll create these forms next

# Dashboard
def dashboard_view(request):
    
    return render(request, 'attendance/dashboard.html')


# View to register individuals
login_required

@login_required
def register_individual(request):
    if request.method == 'POST':
        form = IndividualForm(request.POST)
        if form.is_valid():
            individual = form.save(commit=False)
            individual.created_by = request.user
            individual.save()
            messages.success(request, "Individual registered successfully.")
            return redirect('register_individual')
    else:
        form = IndividualForm()
    return render(request, 'attendance/register_individual.html', {'form': form})

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('create_course')
    else:
        form = CourseForm()
    return render(request, 'attendance/create_course.html', {'form': form})

@login_required
def waiting_list(request):
    if request.method == 'POST':
        form = WaitingListForm(request.POST)
        if form.is_valid():
            waiting_list = form.save(commit=False)
            waiting_list.created_by = request.user
            waiting_list.save()
            messages.success(request, "You have been added to the waiting list.")
            return redirect('waiting_list')
    else:
        form = WaitingListForm()
    return render(request, 'attendance/waiting_list_form.html', {'form': form})

@login_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gates')  # Redirect to dashboard after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'attendance/login.html', {'form': form})




# view to handler user registration

# def register_staff(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'attendance/register_staff.html', {'form': form})