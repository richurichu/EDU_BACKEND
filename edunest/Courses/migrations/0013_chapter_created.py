# Generated by Django 4.2.6 on 2023-10-27 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0012_applications_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
