from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):

    seller_name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    phone = models.CharField(max_length=10)
    De_Neve = models.BooleanField()
    Feast = models.BooleanField()
    Bplate = models.BooleanField()
    Covel = models.BooleanField()

    def __str__(self):
        return self.seller_name + ' ' + str(self.phone)


class PostDate(models.Model):
    post = models.ForeignKey('Post')
    date = models.DateField()


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)





