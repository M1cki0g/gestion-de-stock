from django.shortcuts import render, redirect
from .models import produit
from django.contrib.auth.decorators import login_required
from .forms import gestionProduct
from django.contrib import messages

@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = gestionProduct(request.POST, request.FILES)
        if form.is_valid():
            nom_produit = form.cleaned_data['nom_produit']
            categorie = form.cleaned_data['categorie']
            quantite = form.cleaned_data['quantite']
            description = form.cleaned_data['description']
            image = form.cleaned_data.get('image')
            
            
            product = produit.objects.create(
                    nom_produit=nom_produit,
                    categorie=categorie,
                    quantite=quantite,
                    description=description,
                    image=image
                )
            return redirect('list_produit')
    else:
        form = gestionProduct()
    return render(request, 'ajouter_prd.html', {'form': form})

def list_product(request):
    produits = produit.objects.all()
    return render(request, 'list_prd.html', {'produits': produits})
