# Generated by Django 3.0.3 on 2020-08-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='PERSONAL BLOG', max_length=255),
        ),
    ]