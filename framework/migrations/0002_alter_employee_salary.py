# Generated by Django 5.1.3 on 2024-11-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.CharField(max_length=20),
        ),
    ]
