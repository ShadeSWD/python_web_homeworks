# Generated by Django 4.2.4 on 2023-09-17 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_post_is_published_alter_post_preview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
    ]