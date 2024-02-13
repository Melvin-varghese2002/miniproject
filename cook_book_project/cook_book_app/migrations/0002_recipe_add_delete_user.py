# Generated by Django 5.0 on 2023-12-20 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=300)),
                ('Recipe', models.CharField(max_length=2000)),
                ('Image', models.ImageField(upload_to='None')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]