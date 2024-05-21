

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from django.contrib import messages


def view_project(request):
    # Retrieve the project associated with the current user
    # Assuming there is a ForeignKey field named 'profile' in the Project model
    project = get_object_or_404(Project, profile__user=request.user)

    # If you don't have a ForeignKey to Profile, modify the query accordingly
    # project = get_object_or_404(Project, user=request.user)

    return render(request, 'view_project.html', {'project': project})
@login_required
def add_project(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        link = request.POST.get('link')
        image = request.FILES.get('image')

        Project.objects.create(
            profile=profile,
            title=title,
            description=description,
            link=link,
            image=image
        )

        messages.success(request, 'Project added successfully.')
        return redirect('portfolio')
    return render(request, 'add_project.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                Profile.objects.create(user=user)  # Automatically create a profile for the new user
                messages.success(request, 'You are now registered and can log in')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Adjust this to your home page or dashboard
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.father_name = request.POST['father_name']
        profile.phone_number = request.POST['phone_number']
        profile.email = request.POST['email']
        profile.bio = request.POST['bio']
        profile.location = request.POST['location']
        profile.birth_date = request.POST['birth_date']
        profile.education = request.POST['education']
        profile.work_experience = request.POST['work_experience']
        profile.certifications = request.POST['certifications']
        profile.save()

        messages.success(request, 'Profile updated successfully')
        return redirect('profile')

    return render(request, 'profile.html', {'profile': profile})

@login_required
def portfolio_view(request):
    profile = Profile.objects.get(user=request.user)
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)
