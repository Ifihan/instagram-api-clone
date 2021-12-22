# Generated by Django 4.0 on 2021-12-22 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_posts_images_images_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='images',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='post_likes',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='caption',
            field=models.CharField(max_length=500),
        ),
    ]
