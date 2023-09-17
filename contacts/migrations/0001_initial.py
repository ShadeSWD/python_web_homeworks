# Generated by Django 4.2.4 on 2023-09-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150, verbose_name='country')),
                ('itn', models.CharField(max_length=30, verbose_name='ITN')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
            ],
        ),
    ]
