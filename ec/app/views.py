from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Customer, Product
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request,"app/customerregistration.html", locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bạn đã đăng ký thành công")
        else:
            messages.warning(request,"Thông tin không hợp lệ")
        return render(request,"app/customerregistration.html", locals())

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,"app/profile.html", locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            city = form.cleaned_data["city"]
            mobile = form.cleaned_data["mobile"]

            reg = Customer(user = user, name = name, address = address, city = city, mobile = mobile)
            reg.save()
            messages.success(request, "Chúc mừng! Hồ sơ đã lưu thành công")
        else:
            messages.warning(request, "Thông tin không hợp lệ")
        return render(request,"app/profile.html", locals())

def address (request):
    add = Customer.objects.filter(user = request.user)
    return render(request,"app/address.html",locals())

