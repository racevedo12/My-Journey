from django import forms
from .models import Picture

class CreatePictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ("user", "image_url",)

        # This is to modify our form and add bootstrap classes into the fields

        # Resources: 
        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
        # https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
        
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "user", "type": "hidden"}),
            # "user": forms.Select(attrs={"class": "form-control"}),
            "image_url": forms.Textarea(attrs={"class": "form-control", "placeholder": "Add an image url"}),
        }

class EditPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ("image_url",)
        
        widgets = {
            "image_url": forms.Textarea(attrs={"class": "form-control", "placeholder": "Add an image url"}),
        }