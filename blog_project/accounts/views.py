from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return redirect('home')

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            print(form.errors)
            print(form.non_field_errors())
            if form.is_valid():
                cd = form.cleaned_data

                user = authenticate(request,
                            username=cd['username'],
                            password=cd['password']
                            )

                if user != None:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse("User Not Found!!!")
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')
