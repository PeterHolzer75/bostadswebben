# Generated by Django 4.0.2 on 2022-02-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
