# Generated by Django 5.0.1 on 2024-02-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic_url',
            field=models.CharField(default='img/default_profile_pic.jpg', max_length=2000),
        ),
        migrations.AddField(
            model_name='tutor',
            name='profile_pic_url',
            field=models.CharField(default='img/default_profile_pic.jpg', max_length=2000),
        ),
    ]