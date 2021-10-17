from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

# Importing models
from .models import Picture, Comment

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

    # Overwritting the get_context_data method in order to render our total_likes function
    # from the picture Model, and send it to the picture_details.html 
    
    def get_context_data(self, *args, **kwargs):
        the_picture = get_object_or_404(Picture, id=self.kwargs["pk"])
        total_likes = the_picture.total_likes()
        total_dislikes = the_picture.total_dislikes()

        liked = False
        disliked = False

        if ( the_picture.likes.filter(id=self.request.user.id).exists() ):
            liked = True
        
        elif ( the_picture.dislikes.filter(id=self.request.user.id).exists() ):
            disliked = True

        context = super(PictureDetailView, self).get_context_data()
        
        # The context field works as a dictionary, that's why we can create a new key-value pair
        context["total_likes"] = total_likes
        context["liked"] = liked
        context["total_dislikes"] = total_dislikes
        context["disliked"] = disliked
        
        return context

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

    # Using this variable to see if they currently user logged in already liked the picture
    liked = False

    if ( picture.likes.filter(id=request.user.id).exists() ):
        picture.likes.remove(request.user)
        liked = False

    else:
        # Add the current user who liked the picture into the likes field of the picture.
        picture.likes.add(request.user)
        liked = True

    # Using HttpResponseRedirect from django.http we can just redirect the page 
    # to the same picture details page instead of going back to the home page.
    return HttpResponseRedirect(reverse("picture_detail", args=(str(pk)) ))

def DislikePictureView(request, pk):
   
    picture = get_object_or_404(Picture, id=request.POST.get("picture_id"))
    disliked = False

    if ( picture.dislikes.filter(id=request.user.id).exists() ):
        picture.dislikes.remove(request.user)
        disliked = False

    else:
        picture.dislikes.add(request.user)
        disliked = True

    return HttpResponseRedirect(reverse("picture_detail", args=(str(pk)) ))

class AddCommentView(CreateView):
    model = Comment
    # form_class = CreateCommentForm
    template_name = "my_journey/add_comment.html"
    fields = "__all__"