from django.shortcuts import render, redirect
from .models import Produit, Categorie
from django.contrib.auth.decorators import login_required
from .forms import gestionProduct
from django.contrib import messages
from .forms import CategorieForm
from .forms import Modifier_prd
from django.shortcuts import get_object_or_404

@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = gestionProduct(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            categorie = form.cleaned_data['categorie']
            Produit.objects.create(
                user=request.user,
                nom_produit=form.cleaned_data['nom_produit'],
                categorie=categorie,
                quantite=form.cleaned_data['quantite'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data.get('image')
            )
            messages.success(request, 'Produit ajouté avec succès!')
            return redirect('list_produit')
    else:
        form = gestionProduct(user=request.user)
    return render(request, 'ajouter_prd.html', {'form': form})

@login_required
def list_product(request):
    produits = Produit.objects.filter(user=request.user)
    return render(request, 'list_prd.html', {'produits': produits})

@login_required
def creer_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            nom_categorie = form.cleaned_data['nom']

            if Categorie.objects.filter(nom=nom_categorie, user=request.user).exists():
                messages.error(request, "Cette catégorie existe déjà.")
                redirect('creer_categorie')
            
            else:
                Categorie.objects.create(user=request.user, nom=nom_categorie)
            return redirect('creer_categorie')
    else:
        form = CategorieForm()
    return render(request, 'creer_categorie.html', {'form': form})

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == 'POST':
        form = Modifier_prd(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('list_produit')
    else:
        form = Modifier_prd(instance=produit, user=request.user)

    return render(request, 'modifier_prd.html', {'form': form})

def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('list_produit')
    return redirect('list_produit')
