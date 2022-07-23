from django.urls import URLPattern,path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),  
    path('category',views.category,name='category'),
    path('brands',views.brand,name='brand'),
    path('my-account',views.myaccount,name='myaccount'),
    path('cart',views.cart,name='cart'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)