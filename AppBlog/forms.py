from django import forms 




    
class AeropuertoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    ciudad=forms.CharField(max_length=50)
    comentario=forms.CharField(max_length=50)
    triper=forms.CharField(max_length=50)
    fecha=forms.DateField()
    foto=forms.ImageField()
    
