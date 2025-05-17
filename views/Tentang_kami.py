import streamlit as st

st.title("Tentang Kami")

from forms.saran import saran_form


@st.dialog("Contact Me")
def show_saran_form():
    saran_form()


# SiKopi Profile
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
 st.image("./assets/sikopi1.png", width=230)
with col2:
   st.title("Si Kopi", anchor=False)
   st.write(
      "Need coffe? just contact Si Kopi"
   )
   if st.button("Berikan saran"):
        show_saran_form()


# Informasi lebih Lanjut
st.write("\n")
st.subheader("Lebih banyak tentang kami", anchor=False)
st.write(
    """
    - Hadir sebagai paltform yang mengkhususkan penjualan kopi
    - Kopi yang dijual berasal dari Petani Kopi Wirogomo
    - Memudahkan pembeli untuk memilih jenis kopi yang ingin dibeli
    - Melayani pengiriman seluruh indonesia!
    """
)

