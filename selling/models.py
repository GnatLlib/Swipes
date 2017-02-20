from django.db import models
from django.conf import settings


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


class PostDate(models.Model):
    post = models.ForeignKey('Post')
    date = models.DateField()






