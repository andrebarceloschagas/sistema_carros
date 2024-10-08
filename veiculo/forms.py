from django import forms
from veiculo.models import Veiculo


class FormularioVeiculo(forms.ModelForm):
    class Meta():
        model = Veiculo
        exclude = []
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'combustivel': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }