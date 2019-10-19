from django.db import models

# Create your models here.


class Book(models.Model):

    bookname = models.CharField(max_length=32,unique=True,verbose_name='书名')

    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='定价')

    marketprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='售价')

    pub = models.CharField(max_length=48,verbose_name='出版社')




