# Generated by Django 4.0.3 on 2022-03-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
