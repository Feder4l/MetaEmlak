from django import forms

class IletisimForm(forms.Form):
    ad_soyad = forms.CharField(max_length=100, label='Ad Soyad')
    email = forms.EmailField(label='E-Posta')
    mesaj = forms.CharField(widget=forms.Textarea, label='Mesaj')
