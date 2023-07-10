print("Selamat Datang di ATM BETA")
print("Pilih Option :")
print("1. Cek Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Uang Saya")
option=int(input("Silahkan Pilih Option :"))
if option==1:
	print("Uang Kamu Berjumlah Rp.500.000")
elif option==2:
	print("Uang Kamu Berjumlah Rp.500.000, Kamu Mau Ambil Uang Berapa?")
	print("1. Rp.100.000")
	print("2. Rp.200.000")
	print("3. Rp.300.000")
	print("4. Rp.400.000")
	print("5. Rp.500.000")
	uang=500000
	option2=int(input("Option :"))
	if option2==1:
			hasil1=uang-100000
			print("Uang Kamu Sekarang Bejumlah :",hasil1)
	elif option2==2:
			hasil2=uang-200000
			print("Uang Kamu Sekarang Berjumlah :",hasil2)
	elif option2==3:
			hasil3=uang-300000
			print("Uang Kamu Sekarang Berjumlah :",hasil3)
	elif option2==4:
			hasil4=uang-400000
			print("Uang Kamu Sekarang Berjumlah :",hasil4)
	elif option2==5:
			hasil5=uang-500000
			print("Uang Kamu Sekarang Berjumlah :",hasil5)
elif option==3:
    uang=50000
    print("Uang Kamu Berjumlah Rp.500.000, Kamu Mau Nabung Berapa?")
    option3=int(input("Masukkan Jumlah Uang :"))
    jumlah=uang+option3
    print("Jumlah Uang Kamu Sekarang Adalah" ,jumlah)
else:
    print("Keywoard Anda Salah, Silahkan Ulang Kembali")
