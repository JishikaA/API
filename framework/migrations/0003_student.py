# Generated by Django 5.1.3 on 2024-11-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0002_alter_employee_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mark', models.CharField(max_length=3)),
            ],
        ),
    ]
