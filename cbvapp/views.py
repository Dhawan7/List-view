from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from .models import Collage

class MyCBV(TemplateView):
    template_name= 'index.html'

class collageList(ListView):
    context_object_name = 'collages_list'
    model = Collage
