# Generated by Django 4.0.6 on 2022-10-11 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('bio', models.TextField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(max_length=100)),
                ('social_github', models.CharField(max_length=200)),
                ('social_linkedin', models.CharField(max_length=200)),
                ('social_youtube', models.CharField(max_length=200)),
                ('social_website', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
