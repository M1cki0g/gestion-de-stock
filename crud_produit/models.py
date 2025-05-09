from django.db import models
import datetime
import os
from django.contrib.auth.models import User  



def file_path(instance, filename):
    timenow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Safe filename creation
    filename = f"{timenow}_{filename}"
    return os.path.join('uploads', filename)


class Categorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    # nb_products = models.IntegerField(default=0)

    def __str__(self):
        return self.nom
    
    def get_nb_products(self):
        return self.produit_set.count() 



class Produit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_produit=models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True) 
    quantite=models.IntegerField()
    image=models.ImageField(upload_to=file_path, blank=True, null=True)
    description = models.TextField(blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change = models.IntegerField()  
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produit.nom_produit} ({'+' if self.change > 0 else ''}{self.change})"
 