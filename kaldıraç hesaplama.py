import streamlit as st

st.title(" Kaldıraç Kâr/Zarar Hesaplama")

İşlemler:

1- Long
2- Short
""")


işlem_türü = input("İşlem Seçiniz (1 veya 2) : ")


giris_fiyatı = float(input("Giriş Fiyatınızı Yazınız: "))
cikis_fiyatı = float(input("Çıkış Fiyatınızı Yazınız: "))
kaldirac = float(input("Kaldıraç Oranınızı Yazınız: "))
islem_boyutu = float(input("İşlem Boyutunuzu Yazınız: "))


if işlem_türü=="1":
    pozisyon = (islem_boyutu / giris_fiyatı) * kaldirac
    kar_zarar = (cikis_fiyatı - giris_fiyatı) * pozisyon

elif işlem_türü=="2":
    pozisyon = (islem_boyutu / giris_fiyatı) * kaldirac
    kar_zarar = (giris_fiyatı - cikis_fiyatı) * pozisyon

elif işlem_türü == "1":
    kar_zarar = (cikis_fiyatı - giris_fiyatı) * pozisyon
elif işlem_türü == "2":
    kar_zarar = (giris_fiyatı - cikis_fiyatı) * (islem_boyutu * kaldirac)
else:
    print("Geçersiz işlem seçimi!")
    kar_zarar = None


if kar_zarar is not None:
    if kar_zarar > 0:
        print("Kârınız: +{:.2f}".format(kar_zarar))
    elif kar_zarar < 0:
        print("Zararınız: -{:.2f}".format(abs(kar_zarar)))
    else:
        print("Ne kâr ne zarar, işlem eşit!")

