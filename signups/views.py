from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user - form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, {'form': form})
