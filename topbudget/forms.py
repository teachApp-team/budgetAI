from .models import Spending
from django import forms

class SpendingCreateForm(forms.ModelForm):
  class Meta:
    model = Spending
    fields = ('cost','category','date','cash','card','comment',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
          field.widget.attrs['class'] = 'form-control'

class DetectForm(forms.Form):
  image = forms.ImageField()

class SpendingNewForm(forms.Form):
  category = forms.CharField()
