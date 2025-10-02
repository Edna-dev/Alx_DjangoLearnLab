from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import RegisterForm, ProfileForm

def index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately after registration
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('blog:index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated.')
            return redirect('blog:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

