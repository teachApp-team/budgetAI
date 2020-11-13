from django import forms

class SpendingNewForm(forms.Form):
  category = forms.CharField(label='カテゴリー', max_length=30)
  cost = forms.IntegerField(label='支出額')
  cost = forms.IntegerField(label='支出額')