# Generated by Django 4.0.4 on 2022-05-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubica', '0004_alter_comment_person_alter_post_person_subcube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcube',
            name='people',
        ),
        migrations.AddField(
            model_name='subcube',
            name='people',
            field=models.ManyToManyField(to='cubica.person'),
        ),
    ]