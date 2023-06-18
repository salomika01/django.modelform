from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})
