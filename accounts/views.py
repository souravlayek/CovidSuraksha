from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import DoctorProfile,UserProfile,ShopManagerProfile,MyUser
from .forms import DoctorProfileForm,UserProfileForm,ShopManagerProfileForm,MyUserCreationForm,ContactUsForm

profileformdict = {'doctor':DoctorProfileForm,'user':UserProfileForm,'shopmanager':ShopManagerProfileForm}
profilemodel =  {'doctor':DoctorProfile,'user':UserProfile,'shopmanager':ShopManagerProfile}

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profileview(request, usertype):
    if request.method == 'POST':
        forms = profileformdict[usertype]
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.user = request.user
            instances.save()
            user_instances = request.user
            user_instances.profileupdated = True
            user_instances.save()
            return redirect('home')
    elif not request.user.profileupdated:
        form = profileformdict[usertype]
        return render(request, 'accounts/profile.html', {'form':form})
    else:
        profile = get_object_or_404(profilemodel[usertype], user=request.user)
        return render(request, 'accounts/profile.html', {'profile':profile})


class ContactUsView(CreateView):
    form_class = ContactUsForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/contact.html'
