from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient,PatientInfo
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PatientForm,PatientInfoForm
from django.shortcuts import _get_queryset
from .decorators import alowed_user

class UserPermissionMixin:
    allowed = ['doctor']
    def dispatch(self, request, *args, **kwargs):
        if not request.user.usertype in  self.allowed:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

def get_object_or_notfound(klass, *args, **kwargs):
    queryset = _get_queryset(klass)

    try:
        return queryset.filter(*args, **kwargs)
    except:
        return 'no update here'

class PatientList(LoginRequiredMixin,UserPermissionMixin,  ListView):
    template_name = 'patientinfo/patientlist.html'
    model = Patient
    context_object_name = 'patient'

@login_required()
@alowed_user(allowed=['doctor'])
def PatientCreate(request):
    if request.method == 'POST':
        forms = PatientForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pinfo:patientlist')
    else:
        form = PatientForm
        return render(request, 'patientinfo/create.html', {'form':form})

@login_required()
@alowed_user(allowed=['doctor'])
def PatientInfoUpdate(request, id):
    patient = get_object_or_404(Patient, pk=id)
    if request.method == 'POST':
        forms = PatientInfoForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.updated_by = request.user
            instances.patient = patient
            instances.save()
            return redirect('pinfo:detail', id=id)
    else:
        patientinfo = get_object_or_notfound(PatientInfo, patient=patient) 
        form = PatientInfoForm
        return render(request, 'patientinfo/updateinfo.html', {'form':form,'patient':patient,'patientinfo':patientinfo})


def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = _get_queryset(Patient).filter(
            Q(name__icontains=search_term) |
            Q(username__icontains=search_term) |
            Q(address__icontains=search_term) |
            Q(town__iexact=search_term) |
            Q(district__iexact=search_term) |
            Q(state__iexact=search_term) |
            Q(notes__icontains=search_term)
        )
        context = {
            'search_term': search_term,
            'patient': search_results
        }
        return render(request, 'patientinfo/patientlist.html', context)
    else:
        return redirect('home')