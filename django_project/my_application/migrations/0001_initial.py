# Generated by Django 5.1.4 on 2025-01-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default='', max_length=20)),
                ('Last_Name', models.CharField(default='', max_length=20)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Password', models.CharField(default='', max_length=30)),
                ('Conform_Password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
