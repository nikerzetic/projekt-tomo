# Generated by Django 5.0.4 on 2024-05-27 14:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("expurtka", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="set",
            name="sort",
        ),
    ]
