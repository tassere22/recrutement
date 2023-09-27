# Generated by Django 4.2.5 on 2023-09-25 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('icone', models.ImageField(upload_to='social_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien_profil', models.URLField()),
                ('reseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chercheur.socialnetwork')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('ville', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/')),
                ('description', models.TextField(null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('competence', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
