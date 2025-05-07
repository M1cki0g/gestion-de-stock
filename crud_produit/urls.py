from django.contrib import admin
from django.urls import path,include
from gestion import views
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),  
     path('list_produit/', views.list_product, name='list_produit'), 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)