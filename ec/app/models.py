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
    mobile = models.IntegerField(default=0)   
    city = models.CharField(choices = CITY_CHOICES, max_length=100, null=True)
    #city = models.CharField(max_length=50)
    #zipcode = models.IntegerField()
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


# Thanh toán 

STATUS_CHOICES = (
    ('Da duoc xac nhan', 'Đã được xác nhận'),
    ('Dang dong goi', 'Đang đóng Gói'),
    ('Dang giao', 'Đang giao'),
    ('Da giao', 'Đã giao'),
    ('Da huy', 'Đã hủy'),
    ('Chua xu ly', 'Chưa xử lý'),
)

# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
#     paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Chua xu ly')
    #payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)