from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = models.ImageField(upload_to='property_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default="", blank=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # ✅ Satıcıdan mesaj alanı
    owner_message = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Satıcıdan Mesaj",
        help_text="İlan hakkında ek bilgi veya satıcı notu yazabilirsiniz."
    )

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"
