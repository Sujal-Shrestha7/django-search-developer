# Generated by Django 4.0.6 on 2022-10-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='social_github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='social_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]