import termcolor


sistem = True

# Kitaplari Listele
kitapListesi = []


def main():
    while sistem is True:
        
        global kitapListesi

        choice = 0 # Algoritma => Asagida 4 adet numaralandirilmis islerimiz var bu islerin her biri icin bir fonksiyon tanimlayacagim. Oncelikle kitapEkle fonksiyonu tanimlayacagim: kitapListesi.appen(). Sonrasinda tek bir kitabi aratmak icin bir fonksiyon tanimlayacagim: input("kitap adi giriniz") eger kitap adi listenin icerisinde ise "kitap mevcut" yazdir. Ucuncu adimda print(kitapListesi) komutunu kullanarak listedeki tum kitaplari yazdiracagim. Son olarak uygulamadan cikisi saglamam gerek ancak bunu yapmak icin fonksiyonu while dongusune almaliyim, while True dongusu kullanirim eger 4 yazdirilirsa break komutu ile donguden cikarim.

        print("*** Sistem Yoneticisi ***")
        print("1) Bir kitap ekle")
        print("2) Bir kitap arat")
        print("3) Tum kitaplari arat")
        print("4) Uygulamadan cikis yap")
        print("\n")
        try:
            yazdir = int(input("Lutfen yapmak istediginiz islemin numarasini giriniz: "))
        except ValueError:
            sonuc = termcolor.colored("Lutfen yalnizca sayisal bir deger giriniz.\nUygulamayi tekrardan baslatiniz.", color = "red", on_color = "on_white")

            print(sonuc)

            break
            
        while 1 > yazdir or yazdir > 4:
            uyari = termcolor.colored("LUTFEN GECERLI BIR ISLEM NUMARASI GIRINIZ(1, 2, 3, 4): ",color = "red", on_color = "on_white")
            print(uyari)
            yazdir = int(input("Lutfen yapmak istediginiz islemin numarasini giriniz: "))

        def kitapEkle():
            eklenenKitap = input("Lutfen Eklemek istediginiz kitabin adini giriniz: ")
            kitapListesi.append(eklenenKitap)
            print("Kitabiniz basariyla eklendi.")
  
        def kitapAra():
            kitapAdi = input("Lutfen veri tabaninda  aratmak istediginiz kitabin adini giriniz: ")
            if kitapAdi in kitapListesi:
                print("Kitabiniz veri tabaninda mevcut.")
            else:
                print("Kitabiniz veritabaninda mevcut degil.")
    
        def tumKitaplar():
            print(f"Tum kitaplarin listesi:\n {kitapListesi}")
         

            
        
        if yazdir == 1:
            kitapEkle()
        if yazdir == 2:
            kitapAra()
        if yazdir == 3:
            tumKitaplar()
        if yazdir == 4:
            print("Uygulamadan ciktiniz.")
            break


if __name__ == "__main__": # eger dosyanin adi = "main.py" ise main fonksiyonunu calistir.
    main()
# Uygulamamiz tamamlandi ancak numara girdisine disaridan string bir deger girildigi zaman program duruyor. Bunun yerine kullaniciyi uyarip tekrardan bir girdi girmeye yonlendirebiliriz: Bunun icin try ve except komutlarına ihtiyacimiz olacak. Alabilecegimiz en sık iki hatadan biri az once belirttigim gibi girdi kismina string bir deger girilmesi. Digeri ise girilen degerin 1 den kucuk veya 4 den buyuk olmasidir: Ayni sekil bu kodlarida try ve except bloguna alip kullaniciyi uyaracagiz.

