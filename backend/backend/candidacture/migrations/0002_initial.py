# Generated by Django 4.2.5 on 2023-09-27 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidacture', '0001_initial'),
        ('job_listings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='candidacture',
            name='job_listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_listings.joblisting'),
        ),
        migrations.AddField(
            model_name='candidacture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]