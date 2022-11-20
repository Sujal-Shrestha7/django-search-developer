# Generated by Django 4.0.6 on 2022-10-11 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0007_projects_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profiles'),
        ),
    ]
