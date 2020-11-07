from django.urls import path

from . import views

app_name='topbudget'
urlpatterns = [
    path('', views.SpendingView.as_view(), name="spending"),
    path('income/', views.IncomeView.as_view(), name="income"),
    path('spending-detail/', views.DetailView.as_view(), name="spending_detail"),

    # path('spending/', views.SpendingView.as_view(), name="spending"),
]