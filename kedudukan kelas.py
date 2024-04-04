#Input
markah=int(input("Masukkan markah anda:"))
#Proses
if markah <=40:
    kelas = "Dedikasi"
elif markah <= 60:
    kelas = "Cerdik"
elif markah <= 80:
    kelas = "Bijak"
else:
    kelas = "Amanah"
#Output
print("Anda ditempatkan di kelas",kelas)
