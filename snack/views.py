from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.


class SnackListView(ListView):
    template_name="snack/snack_list.html"
    model=Snack
#_________________________________________

class SnackDetailView(DetailView):
    template_name="snack/snack_detail.html"
    model=Snack
    context_object_name = 'snack_object'
#_________________________________________

class SnackCreateView(CreateView):
    template_name="snack/snack_create.html"
    model=Snack
    fields=['purchaser','name','description']
    
#_________________________________________

class SnackUpdateView(UpdateView):
    template_name = "snack/snack_update.html"
    model = Snack
    fields = ['name', 'description']
#_________________________________________

class SnackDeleteView(DeleteView):
    template_name = "snack/snack_delete.html"
    model = Snack
    fields = ['name', 'description']
    success_url = reverse_lazy('snack_list')

