from accounts.models import CustomUser
from django.db import models

class Card(models.Model):
  name = models.CharField(verbose_name='決済手段名', max_length=20)
  date = models.DateField(verbose_name='引き落とし日', auto_now=False)
  user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.SET_NULL, null=True, blank=True)

  class Meta:
    verbose_name_plural = 'Card'

  def __str__(self):
    return self.name

# Create your models here.
class Spending(models.Model):
  """支出モデル"""
  cost = models.PositiveIntegerField(verbose_name='支出額', default=0)
  category = models.CharField(verbose_name='カテゴリー', max_length=20)
  user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
  date = models.DateField(verbose_name='発生日', auto_now=False)
  cash = models.BooleanField(verbose_name='現金決済')
  card = models.ForeignKey(Card, verbose_name='その他決済', on_delete=models.SET_NULL, null=True, blank=True)
  comment = models.CharField(verbose_name='コメント', max_length=40, null=True, blank=True)
  picture = models.ImageField(upload_to='images/', verbose_name='レシートを読み込む')
  created_at = models.DateTimeField(verbose_name='作成時', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

  class Meta:
    verbose_name_plural = 'Spending'

  def __str__(self):
    return self.category