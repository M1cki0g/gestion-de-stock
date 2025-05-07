from django import forms
from .models import produit

class gestionProduct(forms.Form):
    nom_produit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez le nom du produit'
        })
    )
    
    categorie = forms.ChoiceField(
        choices=produit.x,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    quantite = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez la quantité'
        })
    )
    
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Entrez une description du produit'
        })
    )
