from django.contrib import admin
from .models import ASC, ASCList, Brand, CommodityGroup


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'courier_delivery',
        'created',
    )


@admin.register(ASC)
class ASCAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number_primary',
        'address_primary',
        'city',
        'email',
    )


@admin.register(CommodityGroup)
class CommodityGroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
    )


@admin.register(ASCList)
class ASCListAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'asc',
        'commodity_group',
    )
