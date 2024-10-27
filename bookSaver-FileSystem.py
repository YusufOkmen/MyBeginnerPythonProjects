import termcolor


sistem = True

#Kitap listesi kitaplar.txt de tutulmaktadir.

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
            eklenenKitap = input("Lutfen Eklemek istediginiz kitabin adini giriniz: ").lower()
            with open("kitaplar.txt", "a", encoding="utf-8") as file:
                file.write(f"{eklenenKitap}")
                file.write("\n")
            print("Kitabiniz basariyla eklendi.")
  
        def kitapAra():
            kitapAdi = input("Lutfen veri tabaninda  aratmak istediginiz kitabin adini giriniz: ").lower()
            with open("kitaplar.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            if (kitapAdi+"\n") in lines:
                sonuc = termcolor.colored("     ", color="green", on_color="on_green")
                print(f"{sonuc}    Kitabiniz veri tabaninda mevcut.  {sonuc}")
            elif kitapAdi + "\n" != lines:
                sonuc = termcolor.colored("     ", color="red", on_color="on_red")
                print(f"{sonuc}    Bu kitap veritabanında mevcut değil.    {sonuc}")
            
    
        def tumKitaplar():
            with open("kitaplar.txt", "r", encoding="utf-8") as file:
                sonuc = file.read()
                print(sonuc)

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

# Hata yonlendirmesini de hallettik ancak yapilmasi gereken cok onemli bir sey var. Elimizdeki kitap listesi tek seferlik bir liste yani kod calismayi durdurdugu zaman liste icerisindeki tum veriler siliniyor. Bu sebeple dosya yonetimi yapacagim kitapEkle fonksiyonu ile dosyamizin icine kitap ekleyecegim. Sonrasinda kitap ara kisminda open read yaparak kitabin eger listede ise geri donus yapacagim.Ayriyeten tum kitaplari cagiran fonksiyon icin dogrudan tum kitaplari okutacagim.
