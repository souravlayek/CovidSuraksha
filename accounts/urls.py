from django.urls import path
from .views import SignUpView,ContactUsView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:usertype>', views.profileview, name = 'profile'),
    path('contactus',ContactUsView.as_view() , name = 'contactus'),
]
