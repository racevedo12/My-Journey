from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth import login

# Importing models
from .models import User, Picture

# Importing forms
from .forms import CreatePictureForm, EditPictureForm

# Create your views here.
class UserHomeView(ListView):
    model = Picture
    template_name = "my_journey/user_home_page.html"
    ordering = ("-id")

class PictureDetailView(DetailView):
    model = Picture
    template_name = "my_journey/picture_detail.html"

class AddPictureView(CreateView):
    model = Picture
    form_class = CreatePictureForm
    template_name = "my_journey/add_picture.html"
    
class EditPictureView(UpdateView):
    model = Picture
    form_class = EditPictureForm
    template_name = "my_journey/edit_picture.html"

class DeletePictureView(DeleteView):
    model = Picture
    template_name = "my_journey/delete_picture.html"
    success_url = reverse_lazy("user_home_page")