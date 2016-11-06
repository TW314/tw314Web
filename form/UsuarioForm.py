from django import forms

class UsuarioFormSuporte(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    data_inativacao = forms.DateField(required=False)
    status_ativacao = forms.CharField(required=True)
    empresa = forms.CharField(required=True)

class UsuarioFormAdmin(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    data_inativacao = forms.DateField(required=False)
    status_ativacao = forms.CharField(required=True)
