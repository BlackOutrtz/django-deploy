from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from . import models

class AtoresForm(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',    
            }
        )
    )

    class Meta:
        model = models.Atores
        fields = (
            'primeiro_nome', 'segundo_nome', 'personalidade',
            'idade', 'imagem',  
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        primeiro_nome = cleaned_data.get('primeiro_nome')
        segundo_nome = cleaned_data.get('segundo_nome')

        if primeiro_nome == segundo_nome:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error(
                'primeiro_nome',
                msg        
            )
            self.add_error(
                'segundo_nome',
                msg        
            )



        return super().clean()
    
    def clean_first_name(self):
        primeiro_nome = self.cleaned_data.get('primeiro_nome')

        if primeiro_nome == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        
        return primeiro_nome