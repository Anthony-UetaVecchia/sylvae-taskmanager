from django.shortcuts import render, redirect
from accounts.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form=LoginForms()
    if request.method == "POST":
        form=LoginForms(request.POST)

        if form.is_valid():
            username_login=form['username_login'].value()
            password=form['password'].value()

        user=auth.authenticate(
            request,
            username=username_login,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{username_login} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
        
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    form = RegisterForms()

    if request.method == "POST":
        form = RegisterForms(request.POST)

        if form.is_valid():
            username_register=form.cleaned_data['username_register']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password_1']

            user = User.objects.create_user(
                username=username_register,
                email=email,
                password=password
            )
            messages.success(request, 'Registration completed successfully!')
            return redirect('index')
        
        else:   
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'accounts/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout completed successfully!')
    return redirect('login')