# Generated by Django 4.0.1 on 2022-02-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/4d977849-eb95-42a6-807e-d8573d31237e'),
        ),
    ]
