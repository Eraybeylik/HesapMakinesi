sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

islem = input("""Yapmak istediğiniz işlemi giriniz.
(Toplama = +, Çıkartma = -, Çarpma = *, Bölme = / )
""")

if islem == "+":
    print("Sonuç : " + str(sayi1 + sayi2))

elif islem == "-":
    print("Sonuç : " + str(sayi1 - sayi2))

elif islem == "*":
    print("Sonuç : " + str(sayi1 * sayi2))

elif islem == "/":
    print("Sonuç : " + str(sayi1 / sayi2))
