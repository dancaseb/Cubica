# Generated by Django 4.0.4 on 2022-05-02 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cubica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cubica.person'),
        ),
        migrations.AddField(
            model_name='post',
            name='person',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cubica.person'),
        ),
    ]