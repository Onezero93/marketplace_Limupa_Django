from django.shortcuts import get_object_or_404, render
from .models import Produk, Kategori, Kontak, Profil, Slide, Statis
from cart.models import Transaksi, DetailTransaksi
from django.db.models import Count
from django.views.generic import View
from django.contrib import messages

def beranda(request):
    kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    slider = Slide.objects.filter(aktif=True).order_by('-id')
    jumlahkategori = Kategori.objects.all().annotate(produk_count=Count('produks')).order_by('-id')
    trending = Produk.objects.order_by('-dibeli')
    context = {"judul": "Halaman Beranda",
               "kategori" : kategori,
               "jumlahkategori":jumlahkategori,
               "slide": slider,
               "trending":trending,}
    return render(request, 'beranda.html', context)

def profil(request):
    profil = Profil.objects.all().order_by('-id')[:1]
    context = {"judul": "Halaman Profil",
               "profil":profil,
               }
    return render(request, 'profil.html', context)

class KontakView(View):
    def get(self, request):
        context = {
            'judul': 'Halaman Kontak',
            }
        return render(request, 'kontak.html', context)
    def post(self, request):
        context = {
            'judul': 'Halaman Kontak',
            'data': request.POST,
            'has_error': False
            }
        nama = request.POST.get('nama')
        no_whatsup = request.POST.get('whatsapp')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        pesan = request.POST.get('pesan')
        if nama=="":
            messages.error(request, 'Nama Masih kosong')
            context['has_error'] = True
        if no_whatsup=="":
            messages.error(request, 'No whatsapp Masih kosong')
            context['has_error'] = True
        if subject=="":
            messages.error(request, 'Subject Masih kosong')
            context['has_error'] = True
        if pesan=="":
            messages.error(request, 'Pesan Masih kosong')
            context['has_error'] = True
        if context['has_error']:
            return render(request, 'kontak.html', context, status=400)
        kontak = Kontak.objects.create(nama = nama, email = email,no_whatsup=no_whatsup, subject = subject, isi = pesan )
        kontak.save()
        context = {
            'judul': 'Halaman Kontak',
            'data': "",
            'has_error': False
            }
        messages.success(request, 'Pesan sudah terkirim, silakan tunggu respon selanjutnya!')
        return render(request, 'kontak.html', context, status=400)
                    
def produk(request,kategori_slug,slug):
    produkdetail = get_object_or_404(Produk, slug=slug)
    related = Produk.objects.filter(kategori=produkdetail.kategori.id)
    jml = related.count()
    context = {
        "judul": "Halaman Produk",
        "detailproduk":produkdetail,
        "related":related,
        "jml":jml,}
    return render(request, 'produk.html', context)
def pemesanan(request):
    context = {"judul": "Halaman Pemesanan",}
    return render(request, 'pemesanan.html', context)
def kategori(request, slug):
    kategori = get_object_or_404(Kategori, slug=slug)
    produk = kategori.produks.order_by('-id')
    context = {
        "judul": "Halaman Produk Kategori",
        "detailkategori": produk,
        "categories":kategori,
        }
    return render(request, 'kategori.html', context)

def kategoriberanda(request):
    kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    return {'kategori':kategori}
def modalberita(request):
    modalproduk = Produk.objects.order_by('-id')
    return {'modalproduk':modalproduk}
def statisweb(request):
    statis = Statis.objects.get(id=1) 
    return {'statis':statis}


# Create your views here.
