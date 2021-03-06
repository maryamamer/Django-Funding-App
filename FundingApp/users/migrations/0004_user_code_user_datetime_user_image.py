# Generated by Django 4.0.1 on 2022-02-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_country_user_date_birth_user_facebook_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(default=0, max_length=90),
        ),
        migrations.AddField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/media/55496a88-a21b-4227-af6d-beef10573da5'),
        ),
    ]
