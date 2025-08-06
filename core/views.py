from django.shortcuts import render, get_object_or_404
from .models import Property
from .forms import IletisimForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    properties = Property.objects.all()
    return render(request, 'core/index.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'core/property_detail.html', {'property': property,'request': request})

def iletisim_view(request):
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            ad_soyad = form.cleaned_data['ad_soyad']
            email = form.cleaned_data['email']
            mesaj = form.cleaned_data['mesaj']

            icerik = f"Ad Soyad: {ad_soyad}\nE-posta: {email}\nMesaj:\n{mesaj}"

            send_mail(
                subject='Yeni İletişim Mesajı',
                message=icerik,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return render(request, 'core/iletisim_basarili.html')
    else:
        form = IletisimForm()

    return render(request, 'core/iletisim.html', {'form': form})

def all_properties(request):
    properties = Property.objects.all()

    # Filtreleme için GET parametreleri
    city = request.GET.get('city')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if city and city != 'all':
        properties = properties.filter(city__icontains=city)

    if category and category != 'all':
        properties = properties.filter(category__icontains=category)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Benzersiz şehir ve kategoriler filtre menüsü için
    cities = Property.objects.values_list('city', flat=True).distinct()
    categories = Property.objects.values_list('category', flat=True).distinct()

    return render(request, 'core/all_properties.html', {
        'properties': properties,
        'cities': cities,
        'categories': categories,
        'selected_city': city,
        'selected_category': category,
        'min_price': min_price,
        'max_price': max_price,
    })