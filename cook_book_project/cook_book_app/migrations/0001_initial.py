# Generated by Django 5.0 on 2023-12-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=220)),
                ('last_name', models.CharField(max_length=220)),
                ('username', models.CharField(max_length=220)),
                ('email', models.CharField(max_length=220)),
                ('password1', models.CharField(max_length=220)),
                ('password2', models.CharField(max_length=220)),
            ],
        ),
    ]
