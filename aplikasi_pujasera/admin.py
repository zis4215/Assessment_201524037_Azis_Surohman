from django.contrib import admin
from .models import Barang, Kasir, Tenan, Nota, BarangNota 

class BarangAdmin(admin.ModelAdmin):
    list_display = ('KodeBarang', 'NamaBarang', 'Satuan', 'HargaSatuan', 'Stok')

class KasirAdmin(admin.ModelAdmin):
    list_display = ('KodeKasir', 'Nama', 'HP')

class TenanAdmin(admin.ModelAdmin):
    list_display = ('KodeTenan', 'NamaTenan', 'HP')

class NotaAdmin(admin.ModelAdmin):
    list_display = ('KodeNota', 'KodeTenan', 'KodeKasir', 'TglNota', 'JamNota', 'JumlahBelanja', 'Diskon', 'Total')

class BarangNotaAdmin(admin.ModelAdmin):
    list_display = ('KodeNota', 'KodeBarang', 'JumlahBarang', 'HargaSatuan', 'Jumlah')

admin.site.register(Barang, BarangAdmin)
admin.site.register(Kasir, KasirAdmin)
admin.site.register(Tenan, TenanAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(BarangNota, BarangNotaAdmin)
