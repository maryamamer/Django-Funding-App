# Generated by Django 4.0.1 on 2022-02-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/media/c9c401b4-4e94-4613-9109-76805347fbca'),
        ),
    ]
