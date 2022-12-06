# Generated by Django 4.1.3 on 2022-12-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customer_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(choices=[('Vung Tau', 'Vũng Tàu'), ('Ho Chi Minh', 'Hồ Chí Minh'), ('Ha Noi', 'Hà Nội')], max_length=100),
        ),
    ]