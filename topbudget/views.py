from django.shortcuts import render
from django.views.generic import TemplateView
from fontawesome.fields import IconField
from .models import Spending
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SpendingView(LoginRequiredMixin, TemplateView):
  model = Spending
  template_name = "topbudget/spending.html"

  def get_queryset(self):
    spendings = Spending.objects.filter(user=self.request.user).order_by('-created_at')
    return spendings

class IncomeView(TemplateView):
  template_name = "topbudget/income.html"

class DetailView(TemplateView):
  template_name = "topbudget/spending_detail.html"
  #教材p263-264要参照