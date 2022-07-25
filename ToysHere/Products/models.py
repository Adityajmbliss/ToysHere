from audioop import reverse
from pyexpat import model
from typing import OrderedDict
from django.db import models
from django.utils.html import mark_safe



# Create your models here.

# Homepage banner 
class HomepageBanner(models.Model):
    Banner_img =models.ImageField(upload_to='banner_imgs/')
    Alt_txt = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("HomepageBanner")
        verbose_name_plural = ("HomepageBanners")

    def __str__(self):
        return self.Alt_txt

    def get_absolute_url(self):
        return reverse("HomepageBanner_detail", kwargs={"pk": self.pk})


# creating category models

class Category(models.Model):
    Cat_Name = models.CharField(max_length=250)
    Cat_img = models.ImageField(upload_to='Category_images/')

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        ordering = ['id']

    def __str__(self):
        return self.Cat_Name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.Cat_img.url))

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


# creating brands Model

class Brand(models.Model):
    Brand_Name = models.CharField(max_length=150)
    Brand_img = models.ImageField(upload_to='brand_imgs/')

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.Brand_Name

    def get_absolute_url(self):
        return reverse("Brand_detail", kwargs={"pk": self.pk})


# creating color model

class Color(models.Model):
    Color_Name = models.CharField(max_length=100)
    Color_code = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("Color")
        verbose_name_plural = ("Colors")
        ordering = ["id"]

    def __str__(self):
        return self.Color_Name
    
    def color_bg(self):
        return mark_safe('<div style="height:30px; width:30px; background-color: %s;"></div>' % (self.Color_code))
        
    def get_absolute_url(self):
        return reverse("Color_detail", kwargs={"pk": self.pk})


# creating size model

class Size(models.Model):
    Size_Type = models.CharField(max_length=50)    

    class Meta:
        verbose_name = ("Size")
        verbose_name_plural = ("Sizes")
        ordering =["id"]

    def __str__(self):
        return self.Size_Type

    def get_absolute_url(self):
        return reverse("Size_detail", kwargs={"pk": self.pk})

# creating product model 

class Product(models.Model):
    Product_title = models.CharField(max_length=250)
    Product_img = models.ImageField(upload_to='Product_imgs/')
    Product_desc = models.TextField()
    Product_Brand = models.ForeignKey("Brand", verbose_name=("Brand"), on_delete=models.CASCADE)
    Product_Category = models.ForeignKey("Category", verbose_name=("Category"), on_delete=models.CASCADE)
    Product_Color = models.ForeignKey("Color", verbose_name=("Color"), on_delete=models.CASCADE)
    Product_Size = models.ForeignKey("Size", verbose_name=("Size"), on_delete=models.CASCADE)
    Published = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
        ordering = ["id"]

    def __str__(self):
        return self.Product_title

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


# Products Attribute model 

class ProductsAttribute(models.Model):
    Product = models.ForeignKey("Product", verbose_name=("Product"), on_delete=models.CASCADE)
    Product_Color = models.ForeignKey("Color", verbose_name=("Color"), on_delete=models.CASCADE)
    Product_Size = models.ForeignKey("Size", verbose_name=("Size"), on_delete=models.CASCADE)
    Product_Price = models.PositiveIntegerField()

    

    class Meta:
        verbose_name = ("Products_Attribute")
        verbose_name_plural = ("Products_Attributes")

    def __str__(self):
        return self.Product.Product_title

    def get_absolute_url(self):
        return reverse("Products_Attribute_detail", kwargs={"pk": self.pk})

