# Generated by Django 3.1.7 on 2021-04-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210419_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
