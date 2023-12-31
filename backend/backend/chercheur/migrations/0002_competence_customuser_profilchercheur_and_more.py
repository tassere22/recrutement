# Generated by Django 4.2.5 on 2023-09-27 15:20

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chercheur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_competence', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Adresse e-mail')),
                ('groups', models.ManyToManyField(blank=True, help_text='Groups for the user', related_name='custom_user_chercheur_set', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permissions for the user', related_name='custom_user_chercheur_set', to='auth.permission', verbose_name='Permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profilchercheur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, help_text='Formats autorisés : JPG, JPEG, PNG. Taille maximale : 5 Mo.', null=True, upload_to='profile_photos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('ville', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'], message='Les fichiers autorisés sont au format PDF, DOC ou DOCX.')])),
                ('description', models.TextField(null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('competences', models.ManyToManyField(blank=True, to='chercheur.competence')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chercheur.customuser')),
            ],
        ),
        migrations.RemoveField(
            model_name='socialprofile',
            name='reseau',
        ),
        migrations.RemoveField(
            model_name='socialprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='SocialNetwork',
        ),
        migrations.DeleteModel(
            name='SocialProfile',
        ),
    ]
