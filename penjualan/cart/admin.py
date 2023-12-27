from django.contrib import admin
from .models import Transaksi, DetailTransaksi

class DetailTransaksiAdmin(admin.ModelAdmin):
    list_display = ("no_transaksi", "produk","jumlah",)
admin.site.register(Transaksi)
admin.site.register(DetailTransaksi,DetailTransaksiAdmin)

# Register your models here.
