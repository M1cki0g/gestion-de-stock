from django import forms
from .models import Produit,Categorie
from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class gestionProduct(forms.Form):
    nom_produit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez le nom du produit'
        })
    )
    
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.none(),
        required=False,
        to_field_name='nom',
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
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super().__init__(*args, **kwargs)
        if user:
            # Filter categories by the logged-in user
            self.fields['categorie'].queryset = Categorie.objects.filter(user=user)

class CategorieForm(forms.ModelForm):
     class Meta:
        model = Categorie  # Spécifiez le modèle lié
        fields = ['nom']  # Spécifiez les champs à inclure dans le formulaire
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le nom de la catégorie'
            })
            }
        
        
class Modifier_prd(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom_produit', 'categorie', 'quantite', 'image', 'description']
        widgets = {
            'nom_produit': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Récupérer l'utilisateur depuis les arguments
        super().__init__(*args, **kwargs)
        if user:
            # Filtrer les catégories pour n'afficher que celles créées par l'utilisateur
            self.fields['categorie'].queryset = Categorie.objects.filter(user=user)
