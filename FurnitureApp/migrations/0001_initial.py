# Generated by Django 4.2.11 on 2024-03-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('catagory', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('src', models.CharField(max_length=500)),
            ],
        ),
    ]
