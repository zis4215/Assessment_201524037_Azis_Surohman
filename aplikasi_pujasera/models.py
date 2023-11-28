from django.db import models

class Barang(models.Model):
    KodeBarang = models.CharField(max_length=20, unique=True)
    NamaBarang = models.CharField(max_length=100)
    Satuan = models.CharField(max_length=20)
    HargaSatuan = models.DecimalField(max_digits=10, decimal_places=2)
    Stok = models.PositiveIntegerField()

    def __str__(self):
        return self.NamaBarang

class Kasir(models.Model):
    KodeKasir = models.CharField(max_length=20, unique=True)
    Nama = models.CharField(max_length=100)
    HP = models.CharField(max_length=15)

    def __str__(self):
        return self.Nama


class Tenan(models.Model):
    KodeTenan = models.CharField(max_length=20, unique=True)
    NamaTenan = models.CharField(max_length=100)
    HP = models.CharField(max_length=15)

    def __str__(self):
        return self.NamaTenan


class Nota(models.Model):
    KodeNota = models.CharField(max_length=20, unique=True)
    KodeTenan = models.ForeignKey(Tenan, on_delete=models.CASCADE)
    KodeKasir = models.ForeignKey(Kasir, on_delete=models.CASCADE)
    TglNota = models.DateField()
    JamNota = models.TimeField()
    JumlahBelanja = models.DecimalField(max_digits=10, decimal_places=2)
    Diskon = models.DecimalField(max_digits=5, decimal_places=2)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nota {self.KodeNota}"


class BarangNota(models.Model):
    KodeNota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    KodeBarang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    JumlahBarang = models.PositiveIntegerField()
    HargaSatuan = models.DecimalField(max_digits=10, decimal_places=2)
    Jumlah = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.JumlahBarang} {self.KodeBarang.NamaBarang} di Nota {self.KodeNota.KodeNota}"
