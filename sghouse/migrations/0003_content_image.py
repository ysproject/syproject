# Generated by Django 3.2.2 on 2021-05-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sghouse', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]