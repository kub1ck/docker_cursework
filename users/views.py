from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('files_list')


def logout_user(request):
    logout(request)
    return redirect('login')
