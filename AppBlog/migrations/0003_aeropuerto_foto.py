# Generated by Django 4.2.3 on 2023-09-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_aeropuerto_fecha_aeropuerto_triper_trip_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aeropuerto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
