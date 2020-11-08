from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from fontawesome.fields import IconField
from .models import Spending
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SpendingView(LoginRequiredMixin, TemplateView):
  model = Spending
  template_name = "topbudget/spending.html"
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      spendings = Spending.objects.filter(user=self.request.user).order_by('-created_at') 
      sumcost = 0
      for s in spendings:
        sumcost += s.cost
      context['sumcost'] = sumcost
      context['spendings'] = spendings
      return context
    
  def get_queryset(self, request):
    spendings = Spending.objects.filter(user=self.request.user).order_by('-created_at')
    # return render(request, "topbudget/spending.html", {'name': name})


class IncomeView(TemplateView):
  template_name = "topbudget/income.html"

class DetailView(TemplateView):
  template_name = "topbudget/spending_detail.html"
  #教材p263-264要参照