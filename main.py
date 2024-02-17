def roma_rakami_to_tam_sayi(roma_rakami):

    degerler = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
    }
    
    if not roma_rakami:
        raise ValueError("Boş bir Roma rakamı girilemez.")
    
    for harf in roma_rakami:
        if harf not in degerler:
            raise ValueError(f"Geçersiz Roma rakamı: '{harf}'.")
    
    sonuc = 0
    onceki_deger = 0
    
    for harf in reversed(roma_rakami):
        deger = degerler[harf]
        if deger < onceki_deger:
            sonuc -= deger
        else:
            sonuc += deger
            onceki_deger = deger

    # Dört tane I, V, X, L, C, D veya M olamaz kuralını kontrol et
    for harf in roma_rakami:
        if harf in "IVXLCDM" and roma_rakami.count(harf) > 3:
            raise ValueError(f"{harf} harfi en fazla 3 kere yazılabilir")

    # IX ve IV gibi özel durumları kontrol et
    if "IX" in roma_rakami or "IV" in roma_rakami:
        if len(roma_rakami) > 2 and roma_rakami[-2:] not in ("IX", "IV"):
            raise ValueError("IX ve IV sadece tek başına veya bir sayının sonunda kullanılabilir")

    return sonuc

# Örnek kullanım
while True:
    try:
        roma_rakami = input("Roma rakamını giriniz: ").upper()
        if not roma_rakami.upper() == "Q":
            tam_sayi = roma_rakami_to_tam_sayi(roma_rakami)
            print(f"{roma_rakami.upper()} Roma rakamının karşılığı olan tam sayı: {tam_sayi}", end="\n\n")
            print("Çıkmak için Q/q basınız.")
        else:
            print("Çıkış yapıldı.", end="\n\n")
            break
    except Exception as e:
        print(e)