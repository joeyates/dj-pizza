from django import forms

class PizzaForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    description = forms.CharField(label='Descrizione', required=False, widget=forms.Textarea)

