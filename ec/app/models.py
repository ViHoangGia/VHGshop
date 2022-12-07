from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CITY_CHOICES = (
    ('Vung Tau', 'Vũng Tàu'),
    ('Ho Chi Minh', 'Hồ Chí Minh'),
    ('Ha Noi', 'Hà Nội'),
    ('Da Nang', 'Đà Nẵng')
)

CATEGORY_CHOICES = (
    ('DT', 'Điện Thoại'),
    ('TL', 'Máy tính Bảng'),
    ('LT', 'Laptop'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    # composition = models.TextField(default='')
    # prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    #city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    #zipcode = models.IntegerField()
    city = models.CharField(choices = CITY_CHOICES, max_length=100, null=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
