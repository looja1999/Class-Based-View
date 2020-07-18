from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_here'] ="This is from the context"
        return context 

#LIST AND DETAIL VIEW

from basic_app.models import School
from . import models

class School_ListView(ListView):
    model = models.School
    context_object_name = 'school_list'

class School_DetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = "basic_app/school_detail.html"