# Generated by Django 4.0.6 on 2022-10-12 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profiles_user_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='short_intro',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
