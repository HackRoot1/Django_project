# Generated by Django 4.1.6 on 2023-02-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('subjects', models.CharField(max_length=50)),
            ],
        ),
    ]
