# Generated by Django 4.2.6 on 2023-11-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0016_merge_20231103_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='phonenumber',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AlterField(
            model_name='applications',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]
