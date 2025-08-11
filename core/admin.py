from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]

    # ✅ Liste görünümünde göstermek istediğin alanlar
    list_display = ("title", "price", "city", "owner", "created_at")

    # ✅ Admin formunda gösterilecek alanlar (sıralı)
    fields = (
        "title", 
        "price", 
        "city", 
        "bedrooms", 
        "bathrooms", 
        "image",
        "category",
        "owner", 
        "owner_message",  # Satıcıdan Mesaj alanı
    )

    search_fields = ("title", "city", "owner__username")
    list_filter = ("city", "created_at")

admin.site.register(Property, PropertyAdmin)
