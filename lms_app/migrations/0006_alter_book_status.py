# Generated by Django 5.0.1 on 2024-01-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0005_alter_book_photo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True),
        ),
    ]
