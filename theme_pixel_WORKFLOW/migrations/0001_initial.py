# Generated by Django 4.2.1 on 2023-05-10 19:58

from django.db import migrations, models
import theme_pixel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191)),
                ('image', models.ImageField(blank=True, null=True, upload_to=theme_pixel.models.filepath)),
            ],
        ),
    ]
