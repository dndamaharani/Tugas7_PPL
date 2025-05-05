from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produk.urls')),  # menghubungkan semua rute dari app produk
]
