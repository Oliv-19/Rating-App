# Generated by Django 5.0 on 2024-03-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0014_remove_user_content_comments_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='poster',
            field=models.ImageField(max_length=100000, null=True, upload_to='media'),
        ),
    ]