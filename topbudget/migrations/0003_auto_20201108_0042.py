# Generated by Django 2.2.2 on 2020-11-07 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topbudget', '0002_auto_20201108_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topbudget.Card', verbose_name='その他決済'),
        ),
    ]
