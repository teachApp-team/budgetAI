from django.shortcuts import render
from django.views.generic import TemplateView
from fontawesome.fields import IconField

# Create your views here.
class SpendingView(TemplateView):
  template_name = "topbudget/spending.html"

class IncomeView(TemplateView):
  template_name = "topbudget/income.html"

class DetailView(TemplateView):
  template_name = "topbudget/spending_detail.html"
  #教材p263-264要参照