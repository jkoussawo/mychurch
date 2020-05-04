from django import forms
from captainicc.models import Membre

class MembreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mb_pole'].widget.attrs['style']  = 'height:800px;'

    class Meta:
        model = Membre
        exclude = ['mb_dons','mb_reponse','mb_created_at']