# Generated by Django 3.2 on 2021-05-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_auto_20210523_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='banner')),
            ],
        ),
    ]