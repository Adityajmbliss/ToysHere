from django.contrib import admin
from .models import *

# Register your models here.

# category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Cat_Name','image_tag')

admin.site.register(Category,CategoryAdmin)

# brand model
class BrandAdmin(admin.ModelAdmin):
    list_display =('id','Brand_Name','Brand_img')

admin.site.register(Brand,BrandAdmin)

# color model

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','Color_Name','color_bg')

admin.site.register(Color,ColorAdmin)


# size model 
admin.site.register(Size)


# Product model 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','Product_img','Product_title','Product_Category','Published')
    list_editable = ('Published',)

admin.site.register(Product,ProductAdmin)

#ProductAttribute model
 
class ProductsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','Product','Product_Color','Product_Size','Product_Price')

admin.site.register(ProductsAttribute,ProductsAttributeAdmin)

# Banner Model 
class HomepageBannerAdmin(admin.ModelAdmin):
    list_display = ('id','Banner_img')

admin.site.register(HomepageBanner,HomepageBannerAdmin)

