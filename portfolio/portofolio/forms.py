from django import forms
from .models import Portfolio

class PortfolioForm(forms.Form):
    ad = forms.CharField(label='Ad', max_length=100)
    soyad = forms.CharField(label='Soyad', max_length=100)
    ata_adi = forms.CharField(label='Ata adı', max_length=100)
    doğum_tarixi = forms.DateField(label='Doğum tarixi')
    doğum_yeri = forms.CharField(label='Doğum yeri', max_length=100)
    cinsiyyət = forms.ChoiceField(label='Cinsiyyət', choices=[('k', 'Kişi'), ('q', 'Qadın')])
    aile_vəziyyəti = forms.CharField(label='Ailə vəziyyəti', max_length=100)
    əlaqə_nömrəsi = forms.CharField(label='Əlaqə nömrəsi', max_length=20)
    email = forms.EmailField(label='Email')
    yaşayış_yeri = forms.CharField(label='Yaşayış yeri', max_length=100)
    tehsili = forms.CharField(label='Təhsili', max_length=100)
