from django.shortcuts import render, redirect
from .models import Produit, Categorie, Transaction
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
            # categorie.nb_products += 1
            categorie.save()
            messages.success(request, 'Produit ajouté avec succès!')
            return redirect('list_produit')
    else:
        form = gestionProduct(user=request.user)
    return render(request, 'ajouter_prd.html', {'form': form})



@login_required
def list_product(request):
    categorie_id = request.GET.get('categorie')
    produits = Produit.objects.filter(user=request.user)
    categories = Categorie.objects.filter(user=request.user)
    
    if categorie_id:
        produits = produits.filter(categorie_id=categorie_id)
    
    context = {
        'produits': produits,
        'categories': categories,
        'categorie_selectionnee': categorie_id
    }
    return render(request, 'list_prd.html', context)



@login_required
def categorie_list(request):
    categories=Categorie.objects.filter(user=request.user)
    return render (request, 'list_categorie.html', {'categories': categories})



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
    old_quantite = produit.quantite
    if request.method == 'POST':
        form = Modifier_prd(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            updated_produit = form.save(commit=False)
            new_quantite = updated_produit.quantite
            
            if new_quantite != old_quantite:
                change = new_quantite - old_quantite
                Transaction.objects.create(
                    produit=produit,
                    user=request.user,
                    change=change
                )
                updated_produit.save()
                redirect('list_produit')
                
    else:
        form = Modifier_prd(instance=produit, user=request.user)

    return render(request, 'modifier_prd.html', {'form': form})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transaction.html', {'transactions': transactions})

def modifier_cat(request,cat_id):
    categorie=get_object_or_404(Categorie,id=cat_id)
    if request.method == 'POST':
        form=CategorieForm(request.POST,instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('list_categorie')
    else:
        form=CategorieForm(instance=categorie)
    return render(request,'modifier_categorie.html',{'form':form})
       




def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        # produit.categorie.nb_products -= 1
        produit.categorie.save()
        produit.delete()
        return redirect('list_produit')
    return redirect('list_produit')


def supprimer_cat(request, cat_id):
    categorie = get_object_or_404(Categorie, id=cat_id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('list_categorie')
    return redirect('list_categorie')

def clear_transaction(request):
    # transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        Transaction.objects.filter(user=request.user).delete()
        return redirect('transaction_list')
    return redirect('transaction_list')