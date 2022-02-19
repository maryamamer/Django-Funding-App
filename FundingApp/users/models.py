from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
import uuid

class user(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField('First Name', max_length=20)
    lname = models.CharField('Last Name', max_length=20)
    email = models.EmailField(max_length=20, blank=False, null=False)
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(verbose_name="phone",null=True, validators=[phone_regex], max_length=14)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    date_birth = models.DateField(null=True)
    facebook_link = models.URLField(null=True)
    country = models.CharField(max_length=50, null=True)
    code = models.CharField(default=0, max_length=90)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to=f'images/{uuid.uuid4()}', blank=True)
    # photo = models.ImageField(verbose_name="photo",upload_to='users/images')
    # def create_superuser(self, email, first_name, last_name, phone, password):
    #     user = self.create_user(email=self.normalize_email(email),
    #                             password=password,
    #                             fname=first_name,
    #                             lname=last_name,
    #                             phone=phone)
    #     user.is_admin = True
    #     user.is_active = True
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #     return user

