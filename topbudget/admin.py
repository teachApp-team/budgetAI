from django.contrib import admin

# Register your models here.
from .models import Card
from .models import Spending

admin.site.register(Card)
admin.site.register(Spending)
