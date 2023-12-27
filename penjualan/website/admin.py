from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis
class DataKategoriAdmin(admin.ModelAdmin):#slug terisi langsung tanpa harus menyimpan
    # ini untuk tidak menampilkan data secara langsung -> prepopulated_fields = {"slug": ("nama",)} 
    list_display = ("nama", "aktif","banner_satu","banner_dua",)
    prepopulated_fields = {"slug": ("nama",)} 
class DataKontakAdmin(admin.ModelAdmin):
    list_display = ("nama", "no_whatsup","email",)
class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk","kategori", "gambar","gambar_satu","gambar_dua","gambar_tiga","gambar_empat","gambar_lima","harga","no_whatsup","diskon","dibeli")
    prepopulated_fields = {"slug": ("nama_produk",)} 
class DataProfilAdmin(admin.ModelAdmin):
    list_display = ("nama", "gambar","tanggal_upload",)
class DataSlideAdmin(admin.ModelAdmin):
    list_display = ("gambar_slide",)
class DataStatisAdmin(admin.ModelAdmin):
    list_display = ("email", "telpon","alamat_kami",)
admin.site.register(Kategori,DataKategoriAdmin)
admin.site.register(Produk,DataProdukAdmin)
admin.site.register(Slide,DataSlideAdmin)
admin.site.register(Kontak,DataKontakAdmin)
admin.site.register(Profil,DataProfilAdmin)
admin.site.register(Statis,DataStatisAdmin)

# Register your models here.
