# Generated by Django 5.0.7 on 2024-07-29 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_alter_post_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
    ]
