# Generated by Django 3.2.12 on 2022-02-13 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('location', models.CharField(default='Mombasa, Likoni', max_length=100)),
                ('capacity', models.DecimalField(decimal_places=0, default=0, max_digits=8)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
