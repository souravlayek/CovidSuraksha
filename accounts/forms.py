from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser,DoctorProfile,UserProfile,ShopManagerProfile,ContactUs


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'usertype','email', 'first_name', 'last_name')
        help_texts = {
            'username' : None,
            'password1' : None
        }


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'usertype')

class ShopManagerProfileForm(ModelForm):
    class Meta:
        model = ShopManagerProfile
        fields = ['profilepic', 'address', 'town', 'district','state','pin']

class DoctorProfileForm(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['designation', 'hospital_name', 'specialist_in', 'profilepic', 'address', 'town','district','state','pin']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['occupation','profilepic', 'address', 'town', 'district','state','pin','notes']

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        widgets = {
            'massage' : forms.Textarea(attrs={
                'placeholder': "Enter Your Massage Here"
            })
        }
        fields = ['name','email', 'massage']