import streamlit as st

st.title("Kaldıraç Kâr/Zarar Hesaplama")

# İşlem türü seçimi
işlem_türü = st.radio("İşlem Türü Seçiniz:", ["Long", "Short"])

# Giriş değerleri
giris_fiyatı = st.number_input("Giriş Fiyatınızı Yazınız:", min_value=0.0, format="%.8f")
cikis_fiyatı = st.number_input("Çıkış Fiyatınızı Yazınız:", min_value=0.0, format="%.8f")
kaldirac = st.number_input("Kaldıraç Oranınızı Yazınız:", min_value=1.0, format="%.2f")
islem_boyutu = st.number_input("İşlem Boyutunuzu Yazınız:", min_value=0.0, format="%.2f")

# Hesaplama butonu
if st.button("Hesapla"):
    if işlem_türü == "Long":
        pozisyon = (islem_boyutu / giris_fiyatı) * kaldirac
        kar_zarar = (cikis_fiyatı - giris_fiyatı) * pozisyon

    elif işlem_türü == "Short":
        pozisyon = (islem_boyutu / giris_fiyatı) * kaldirac
        kar_zarar = (giris_fiyatı - cikis_fiyatı) * pozisyon

    else:
        st.error("Geçersiz işlem seçimi!")
        kar_zarar = None

    # Sonucu gösterme
    if kar_zarar is not None:
        if kar_zarar > 0:
            st.success(f"Kârınız: +{kar_zarar:.2f}")
        elif kar_zarar < 0:
            st.error(f"Zararınız: -{abs(kar_zarar):.2f}")
        else:
            st.info("Ne kâr ne zarar, işlem eşit!")




