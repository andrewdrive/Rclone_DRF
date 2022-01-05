# Generated by Django 3.2.8 on 2021-10-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20211027_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('host', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]
