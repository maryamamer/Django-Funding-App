# Generated by Django 4.0.1 on 2022-02-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/4fe79d8e-c4f9-4900-9aae-61788fc39a10'),
        ),
    ]
