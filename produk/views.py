from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Selamat datang di Homepage Katalog!</h1>")

def daftar_produk(request):
    return HttpResponse("<h1>Daftar Produk</h1><ul><li>Produk 1</li><li>Produk 2</li></ul>")

def detail_produk(request, produk_id):
    return HttpResponse(f"<h1>Detail Produk {produk_id}</h1><p>Deskripsi produk ID {produk_id}.</p>")

def kontak(request):
    return HttpResponse("<h1>Kontak Kami</h1><p>Email: kontak@katalog.com</p>")
