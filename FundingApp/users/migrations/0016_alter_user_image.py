# Generated by Django 4.0.1 on 2022-02-12 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/00c3fcbe-721f-4c7e-ae70-755f1a1fbdc6'),
        ),
    ]
