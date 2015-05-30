from django.contrib import admin
from backend.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(BankAccount)
admin.site.register(MonetaryDonation)
admin.site.register(VolunteeringPledge)
admin.site.register(Tag)

class BankAccountInline(admin.TabularInline):
    model = BankAccount
    extra = 1

class CivilAssociationAdmin(admin.ModelAdmin):
    inlines = [BankAccountInline]
    list_display = ('name', 'founded_in', 'address', 'category')
    search_fields = ['name']

admin.site.register(CivilAssociation, CivilAssociationAdmin)