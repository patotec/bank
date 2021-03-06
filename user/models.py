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
    avaliablebalance = models.CharField(max_length=50,default='0')
    curentbalance = models.CharField(max_length=50,default='0')
    checkingbalance = models.CharField(max_length=50,default='10')
    accnumber = models.CharField(max_length=10,blank=True)
    acctype = models.CharField(max_length=10,blank=True)
    image = models.ImageField(default='pro_ny6h2o.png',blank=True)
    def __str__(self):
        return self.username



class Otp(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    otp = models.CharField(max_length=10,default='0')
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


class Withdraw(models.Model):
    accountname = models.CharField(max_length=50,default='0')
    accountnumber = models.CharField(max_length=50,default='0')
    bankname = models.CharField(max_length=50,default='0')
    pin = models.CharField(max_length=10,default='0')

    def __str__(self):
        return self.accountname
        
class Tran(models.Model):
    name = models.CharField(max_length=50,default='0')
    dis = models.CharField(max_length=50,default='0',blank=True)
    price = models.CharField(max_length=50,default='0')
    status = models.CharField(max_length=50,default='Paid')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


# class Pay_method(models.Model):
#     name = models.CharField(max_length=50,default='0')
#     wallet = models.CharField(max_length=500,default='0')
#     image = models.FileField()
#     visible = models.BooleanField(default=True)
#     slug = models.SlugField(blank=True)
#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Pay_method, self).save(*args, **kwargs)

class Payment(models.Model):
    user = models.CharField(max_length=50,default='0')
    image = models.FileField()
    approve = models.BooleanField(default=False)
    def __str__(self):
        return self.name