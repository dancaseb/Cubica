# Generated by Django 4.0.4 on 2022-05-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubica', '0022_alter_message_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date sent'),
        ),
    ]
