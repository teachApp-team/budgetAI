from django.shortcuts import render
from django.views import generic
from .forms import SignupForm 

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

class SignupView(generic.FormView):
  template_name = 'signup.html'
  form_class = SignupForm
