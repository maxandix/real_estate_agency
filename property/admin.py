from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat']
    list_display = ['author', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ['id', 'full_name', 'owners_phonenumber', 'owners_phonenumber_pure']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
