# Generated by Django 3.1.7 on 2021-04-19 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210419_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
