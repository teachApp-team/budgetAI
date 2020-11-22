from .models import Spending
from django import forms

class SpendingCreateForm(forms.ModelForm):
  class Meta:
    model = Spending
    fields = ('cost','category','date','cash','card','comment','picture')
    cost = forms.IntegerField()
    category = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    cash = forms.ModelChoiceField(label='現金払い',queryset=None)
    card = forms.ModelChoiceField(label='カード払い',queryset=None)
    picture = forms.ImageField(label='レシートを読み込む')
    comment = forms.CharField()
    widgets = {
      'date': forms.SelectDateWidget
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
          field.widget.attrs['class'] = 'form-control'

class DetectForm(forms.Form):
  image = forms.ImageField()

class SpendingNewForm(forms.Form):
  category = forms.CharField()
