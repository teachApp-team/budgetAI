from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from fontawesome.fields import IconField
from .models import Spending
from .forms import SpendingNewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SpendingCreateForm, DetectForm
from django.urls import reverse_lazy
from django.contrib import messages

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

class DetailView(LoginRequiredMixin, DetailView):
  model = Spending
  template_name = "topbudget/spending_detail.html"
  #教材p263-264要参照

class SpendingCreateView(LoginRequiredMixin, CreateView):
  model = Spending
  template_name = "topbudget/spending_create.html"
  form_class = SpendingCreateForm
  success_url = reverse_lazy('topbudget:spending')

  def form_valid(self, form):
    spending = form.save(commit=False)
    spending.user = self.request.user
    spending.save()
    messages.success(self.request, '領収書を記録しました')
    return super().form_valid(form)

class SpendingDetectView(TemplateView):
  template_name = "topbudget/detect_recipt.html"
#   def post(self, req):
#     form = DetectForm(req.Post, req.FILES)
#     if not form.is_valid():
#       raise ValueError('invalid form')

#     image = form.cleaned_data['image']
#     self.params['pred'] = pred(image)
#     return render(req, 'myapp/index.html', self.params)

