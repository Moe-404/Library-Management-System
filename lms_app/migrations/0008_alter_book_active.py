# Generated by Django 5.0.1 on 2024-01-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0007_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
