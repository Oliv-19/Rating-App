# Generated by Django 5.0 on 2024-01-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_alter_content_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
