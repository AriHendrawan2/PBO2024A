import random
print("SELAMAT DATANG DI LOVEMETER")

nama_dia = input("Masukkan nama dia")
cocok = random.random()

print("kecocokan anda" , cocok * 100, "%")
if cocok > 0.8:
    print("anda sangat cocok dengan " + nama_dia + "!")
elif 0.5 <= cocok <= 0.8 :
    print("anda lumayan cocok dengan " + nama_dia + "!")
else:
    print("anda tidak cocok dengan " +  nama_dia + " :(")