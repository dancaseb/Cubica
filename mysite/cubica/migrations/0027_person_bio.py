# Generated by Django 4.0.4 on 2022-05-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubica', '0026_subcube_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.CharField(default='', max_length=400),
        ),
    ]
