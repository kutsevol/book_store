# Generated by Django 2.1.1 on 2018-09-16 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
