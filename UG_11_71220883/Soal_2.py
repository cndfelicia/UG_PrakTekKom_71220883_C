print("Pemeriksaan Kelipatan 9")
a=int(input("Masukkan angka kelipatan 9 yang ingin di periksa: "))
def kelipatan_9():
    hasil=(a%9)
    return hasil
if kelipatan_9()==0:
    print("BENAR")
else:
    print("SALAH")
