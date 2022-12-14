# Generated by Django 4.1.3 on 2022-12-09 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Da duoc xac nhan', 'Đã được xác nhận'), ('Dang dong goi', 'Đang đóng Gói'), ('Dang giao', 'Đang giao'), ('Da giao', 'Đã giao'), ('Da huy', 'Đã hủy'), ('Chua xu ly', 'Chưa xử lý')], default='Chua xu ly', max_length=50),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
