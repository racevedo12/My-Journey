from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

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

def LikePictureView(request, pk):
    # Resource:
        # https://docs.djangoproject.com/en/3.2/intro/tutorial04/

    # Uses the get_object_or_404 function that gets the Picture model
    # And for the id it uses it's for the name attribute for the picture_id that we use in the picture_detail.html like button from the form
    picture = get_object_or_404(Picture, id=request.POST.get("picture_id"))

    # Then add the current user who liked the picture into the likes field of the picture.
    picture.likes.add(request.user)

    # Using HttpResponseRedirect from django.http we can just redirect the page 
    # to the same picture details page instead of going back to the home page.
    return HttpResponseRedirect(reverse("picture_detail", args=(str(pk)) ))