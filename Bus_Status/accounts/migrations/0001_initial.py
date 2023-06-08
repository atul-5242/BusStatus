# Generated by Django 4.1.3 on 2023-01-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_here', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=35)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]
