from django import forms
from .models import Picture, Comment

class CreatePictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ("user", "image_url",)

        # This is to modify our form and add bootstrap or any css classes into the fields

        # Resources: 
        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
        # https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
        
        widgets = {
            # Added an id for the user in order to select it using DOM manipulation into the script tag from the add_picture.html
            "user": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "user", "type": "hidden"}),
            "image_url": forms.Textarea(attrs={"class": "form-control", "placeholder": "Add an image url"}),
        }

class EditPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ("image_url",)
        
        widgets = {
            "image_url": forms.Textarea(attrs={"class": "form-control", "placeholder": "Add an image url"}),
        }

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", "name",)
        
        widgets = {

            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type in your comment"} ),

            "name": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "user", "type": "hidden"}),
        }