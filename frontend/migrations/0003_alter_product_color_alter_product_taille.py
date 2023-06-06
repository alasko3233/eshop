# Generated by Django 4.1.7 on 2023-05-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_category_image_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='taille',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
