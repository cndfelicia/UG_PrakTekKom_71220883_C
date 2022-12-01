print("=========================")
print("Operasi Matematika")
print("1. Jumlah [+]")
print("2. Kurang [-]")
print("3. Kali   [*]")
print("4. Bagi   [/]")
print("=========================")
pilihan=input("Pilih operasi (1/2/3/4): ")
print("=========================")
pertama=int(input("Masukkan bilangan pertama: "))
kedua=int(input("Masukkan bilangan kedua: "))

def penjumlahan(pertama,kedua):
    jumlah=pertama+kedua
    return jumlah
def pengurangan(pertama,kedua):
    kurang=pertama-kedua
    return kurang
def perkalian(pertama,kedua):
    kali=pertama*kedua
    return kali
def pembagian(pertama,kedua):
    bagi=pertama/kedua
    return bagi

if pilihan==1:
    print("Hasil operasi dari ",pertama,"+",kedua,"=",penjumlahan(pertama,kedua))
elif pilihan==2:
    print("Hasil operasi dari ",pertama,"-",kedua,"=",pengurangan(pertama,kedua))
elif pilihan==3:
    print("Hasil operasi dari ",pertama,"*",kedua,"=",perkalian(pertama,kedua))
elif pilihan==4:
    print("Hasil operasi dari ",pertama,"/",kedua,"=",pembagian(pertama,kedua))
