# Generated by Django 5.0 on 2024-02-05 13:56

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_alter_content_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user_content_id',
        ),
        migrations.RemoveField(
            model_name='user_content',
            name='user_content_id',
        ),
        migrations.AddField(
            model_name='user_content',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_content',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_id',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='user_content',
            name='comments_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ratings.comments'),
        ),
        migrations.AlterField(
            model_name='user_content',
            name='content_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ratings.content'),
        ),
        migrations.AlterField(
            model_name='user_content',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_content',
            name='review',
            field=models.TextField(max_length=250),
        ),
    ]
