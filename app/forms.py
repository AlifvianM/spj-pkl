from django import forms
from .models import Spj, TanggalMerah

class SpjForm(forms.ModelForm):
    nama_spj = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
        , max_length=255, required=False
        )
    pembuat = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
        , max_length=255, required=False
        )

    class Meta:
        model = Spj
        fields = (
            "nama_spj",
            "pembuat"
            )

class TanggalMerahForm(forms.ModelForm):

    tanggal_merah = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs = {
                'type':'date'
            }
        )
        )

    class Meta:
        model = TanggalMerah
        fields = (
            'tanggal_merah',
        )
