# Generated by Django 4.0.6 on 2022-11-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False, null=True),
        ),
    ]