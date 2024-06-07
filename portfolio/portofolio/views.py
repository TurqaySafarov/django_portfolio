from django.shortcuts import render
from .forms import PortfolioForm

def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            ad = form.cleaned_data['ad']
            soyad = form.cleaned_data['soyad']
            ata_adi = form.cleaned_data['ata_adi']
            doğum_tarixi = form.cleaned_data['doğum_tarixi']
            doğum_yeri = form.cleaned_data['doğum_yeri']
            cinsiyyət = form.cleaned_data['cinsiyyət']
            aile_vəziyyəti = form.cleaned_data['aile_vəziyyəti']
            əlaqə_nömrəsi = form.cleaned_data['əlaqə_nömrəsi']
            email = form.cleaned_data['email']
            yaşayış_yeri = form.cleaned_data['yaşayış_yeri']
            tehsili = form.cleaned_data['tehsili']
            
            return render(request, 'success.html')  
    else:
        form = PortfolioForm()
    return render(request, 'portfolio_create.html', {'form': form})
