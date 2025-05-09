from django.contrib import admin
from django.urls import path,include
from gestion import views
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),  
    path('list_produit/', views.list_product, name='list_produit'),
        path('list_categorie/', views.categorie_list, name='list_categorie'),
    path('creer_categorie/', views.creer_categorie, name='creer_categorie'),
    path('list_produit/modifier_prd/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('list_produit/supprimer_prd/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
     path('<int:cat_id>', views.modifier_cat, name='modifier_cat'),
    path('/<int:cat_id>/', views.supprimer_cat, name='supprimer_cat'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)