# Generated by Django 4.1.1 on 2022-09-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapi', '0003_alter_product_name_alter_product_picture1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture1',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='photos'),
        ),
    ]