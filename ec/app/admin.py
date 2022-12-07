from django.contrib import admin
from . models import Cart, Customer, Product

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'mobile', 'address', 'city']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

#Phần thanh toán chưa được vì phải đăng ký tài khoản thanh toán online

# @admin.register(Payment)
# class PaymentModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status' ,'razorpay_payment_id', 'paid']

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment'] 