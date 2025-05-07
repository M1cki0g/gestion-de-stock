from django.db import models
from django.utils import timezone
import datetime
import os


def file_path(instance, filename):
    timenow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Safe filename creation
    filename = f"{timenow}_{filename}"
    return os.path.join('uploads', filename)

class produit(models.Model):
    x=[('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food'),
        ('Books', 'Books'),
        ('Other', 'Other'),]
    nom_produit=models.CharField(max_length=100)
    categorie=models.CharField(choices=x , max_length=100)
    quantite=models.IntegerField()
    image=models.ImageField(upload_to=file_path, blank=True, null=True)
    description = models.TextField(blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)



