from django.urls import path
from . import views
from .views import PatientList,PatientCreate,PatientInfoUpdate,search

urlpatterns = [
    path('patientlist/',PatientList.as_view(),name='patientlist'),
    path('detail/<int:id>/', PatientInfoUpdate, name="detail"),
    path('create/',PatientCreate,name='create'),
    path('search/',search,name='search'),

]
