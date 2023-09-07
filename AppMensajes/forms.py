from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class MensajeForm(forms.Form):
    receptor = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)

    def clean_receptor(self):
        receptor_username = self.cleaned_data['receptor']
        try:
            receptor = User.objects.get(username=receptor_username)
        except User.DoesNotExist:
            raise forms.ValidationError('El receptor no existe.')
        return receptor_username