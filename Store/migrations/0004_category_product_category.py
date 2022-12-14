# Generated by Django 4.1.2 on 2022-11-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_order_address_order_city_order_paid_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='product', to='Store.category'),
        ),
    ]
