from django.db import models
# from accounts.models import User
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @classmethod
    def updateprice(cls, prod_id, price):
        p = cls.objects.filter(pk=prod_id)
        p = p.first()
        p.price=price
        p.save()
        return p
    
    @classmethod
    def create(cls, product_name, price):
        p = Product(name=product_name, price=price)
        p.save()
        return p

class CartManager(models.Manager):
    def create_cart(self, user):
        c = self.create(user=user)
        c.save()
        return c
  
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now())

    objects = CartManager()

    def __str__(self):
        return self.user.get_username()

class ProductInCart(models.Model):
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = (('cart', 'product'),)

class Order(models.Model):
    status_choices = (
        (1, 'start'),
        (2, 'progress'),
        (3, 'done'),
    )
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(choices=status_choices, default=1)

class Deal(models.Model):
  user = models.ManyToManyField(settings.AUTH_USER_MODEL)
  deal_name = models.CharField(max_length=200)

