import random

# Sahte isim oluşturmak isteyip istemediğini soruyoruz
ad = input("Sahte İsim mi Oluşturmak İstiyorsunuz ? (evet/hayır) : ").lower()

if ad == "evet":
    def isim_olustur():
        # Kadın isimleri listesi
        kadin_isimleri = [
            "JALE", "GAMZE", "BEDRİYE MÜGE", "BİRSEN", "REYHAN", "GÜLŞAH", "NALAN", "ŞENAY", 
            "IRAZCA", "HATİCE", "REZAN", "PINAR", "MESUDE", "TÜMAY", "EVRİM", "ÜLKÜ", "BURCU", 
            "FULYA", "ZEYNEP", "AYŞEGÜL", "GÜLAY", "RABİA", "SEVDA", "TUBA", "TUBA HANIM", "MEHRİ", 
            "MEHMET FERHAT", "ÖZGÜR SİNAN", "ASUDAN TUĞÇE", "DİLEK", "SULTAN", "CEREN", "MERAL LEMAN", 
            "BENGÜ", "BİRİGÜL", "ŞEYMA", "ZÜMRÜT ELA", "MERYEM"
        ]
        
        # Erkek isimleri listesi
        erkek_isimleri = [
            "ALİ", "MAHMUT", "MANSUR KÜRŞAD", "YÜCEL", "KUBİLAY", "HAYATİ", "SERDAL", "BÜNYAMİN", 
            "ÖZGÜR", "FERDİ", "İLHAN", "SEMİH", "ERGÜN", "FATİH", "SERKAN", "EMRE", "BAHATTİN", "FUAT", 
            "MEHMET", "EVREN", "OKTAY", "HARUN", "YAVUZ", "UMUT", "TUFAN AKIN", "TURGAY YILMAZ", "GÜLDEHEN", 
            "AHMET", "HÜSEYİN YAVUZ", "BAŞAK", "AYDIN", "SELÇUK", "MEHMET", "NEZİH", "MUSTAFA", "TİMUR", 
            "ERHAN", "MUTLU", "MEHMET HÜSEYİN", "İSMAİL EVREN", "MESUT", "MEHMET HİLMİ", "AHMET GÖKHAN", 
            "BÜLENT", "HARUN", "MEHMET ALİ"
        ]
        
        # Kadın soyisimleri ve erkek soyisimleri
        kadin_soyisimleri = [
            "Kaya", "Öztürk", "Yılmaz", "Çelik", "Demir", "Şahin", "Koç", "Aksoy", "Aydın", "Bayram", 
            "Çakır", "Arslan", "Duman", "Büyük", "Toprak", "Süleyman", "Ceylan", "Bulut", "Gül", "Bahar", 
            "İlhan", "Turan", "Kurt", "Başar", "Özer", "Acar", "Arıkan", "Albayrak", "Sezer", "Yavuz"
        ]
        
        erkek_soyisimleri = [
            "Yılmaz", "Kara", "Demir", "Arslan", "Çelik", "Şahin", "Aksoy", "Çetin", "Öztürk", "Aydın", 
            "Çakır", "Koç", "Büyüktürk", "Özer", "Kurt", "Altun", "Kılıç", "Can", "Türker", "İsmailoğlu", 
            "Vural", "Özdemir", "Ersoy", "Gökhan", "Kumru", "Eroğlu", "Turan", "Sevgi", "Süleyman", "Savaş", 
            "Güner"
        ]
        
        # Kadın ve erkek isimlerinden rastgele seçim yapalım
        isim = ""
        soyisim = ""
        gender_choice = random.choice(["kadın", "erkek"])  # Kadın ya da erkek seçimi
        
        if gender_choice == "kadın":
            isim = random.choice(kadin_isimleri)
            soyisim = random.choice(kadin_soyisimleri)
        else:
            isim = random.choice(erkek_isimleri)
            soyisim = random.choice(erkek_soyisimleri)

        return "{} {}".format(isim, soyisim)

    try:
        adet = int(input("Kaç tane isim soyisim üretmek istersiniz? : "))
        if adet > 1:
            print("Sahte İsimleriniz Oluşturuluyor...")
        else:
            print("Sahte İsminiz Oluşturuluyor...")
        
        for _ in range(adet):
            print(isim_olustur())
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
else:
    print("Uygulama Kapatılıyor..")
