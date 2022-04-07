from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50,default='0')
    totalprofit = models.CharField(max_length=50,default='0')
    totaldeposit = models.CharField(max_length=50,default='0')
    accountbalance = models.CharField(max_length=50,default='10')
    is_email_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Withdraw(models.Model):
	accountname = models.CharField(max_length=50,default='0')
	accountnumber = models.CharField(max_length=50,default='0')
	routingnumber = models.CharField(max_length=50,default='0')

	def __str__(self):
		return self.accountname
class Plan(models.Model):
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    def __str__(self):
        return self.name


class Pay_method(models.Model):
    name = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.FileField()
    visible = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pay_method, self).save(*args, **kwargs)

class Payment(models.Model):
    user = models.CharField(max_length=50,default='0')
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.FileField()
    approve = models.BooleanField(default=False)
    def __str__(self):
        return self.name