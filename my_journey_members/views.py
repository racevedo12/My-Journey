from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"

    # Using reverse_lazy to provide a reverse url(redirect) to the login template that django has built in
    # https://docs.djangoproject.com/en/3.2/ref/urlresolvers/
    success_url = reverse_lazy("login")