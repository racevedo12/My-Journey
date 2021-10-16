from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    # Django Documentation
    # Resource:
        # https://docs.djangoproject.com/en/3.2/ref/forms/widgets/

    first_name = forms.CharField(max_length=50, widget=forms.TextInput( attrs={"class": "form-control"} ))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput( attrs={"class": "form-control"} ))
    email = forms.EmailField( widget=forms.EmailInput( attrs={"class": "form-control"} ) )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

    # Resource for adding styles into the UserCreationForm fields:
        # https://stackoverflow.com/questions/56743425/is-there-a-way-i-can-add-a-class-or-id-to-a-form-generated-with-usercreationform

    # After reading that resource from stackoverflow I realized that you can inherit all the fields
    # and edit them by using self.fields and selecting the field that you want in brackets
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"