# Generated by Django 5.0 on 2024-01-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_alter_content_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
