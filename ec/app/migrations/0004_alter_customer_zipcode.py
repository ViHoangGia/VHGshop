# Generated by Django 4.1.3 on 2022-12-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(choices=[('Vung Tau', 'Vung Tau'), ('Ho Chi Minh', 'Ho Chi Minh'), ('Ha Noi', 'Ha Noi')], max_length=100),
        ),
    ]
