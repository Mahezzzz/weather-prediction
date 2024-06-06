import streamlit as st

st.set_page_config(
    page_title="Weather Prediction",
    page_icon="✨"
)
st.title("Halo, Selamat Datang di Aplikasi Prediksi Cuaca!")
st.header("Ini adalah halaman beranda, harap pilih menu untuk melanjutkan.")
st.sidebar.write("Silahkan Pilih Menu")

st.image("cuaca 4.png", use_column_width=True)
# Add custom CSS to style the app
st.markdown("""
    <style>
    /* CSS untuk latar belakang */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(#80c8ff,#a6d9ff,#b9e1ff,#e4f3ff); 
    }
        [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);      
    }
    h1 {
        color: #1a4b94; /* Warna teks judul */
    }
    h2 {
        color: #2775bf; /* Warna teks judul */
    /* CSS untuk desain sidebar */
    /* CSS untuk desain sidebar */
    }
        [data-testid="stSidebar"] {
        background: linear-gradient(#fff394,#fff9e2);
        color: #1a4b94;
        padding: 20px;               
    }
.sidebar .sidebar-content {
    background-color: #1a4b94; /* Warna latar belakang sidebar */
    color: #1a4b94; /* Warna teks di sidebar */
    padding: 20px; /* Padding konten sidebar */
}

.sidebar .sidebar-content a {
    color: #1a4b94; /* Warna tautan di sidebar */
    text-decoration: none; /* Hilangkan garis bawah pada tautan */
    display: block; /* Tampilkan dalam blok */
    padding: 10px 0; /* Padding tautan */
}

.sidebar .sidebar-content a:hover {
    background-color: #555; /* Warna latar belakang saat tautan dihover */
}

.sidebar .sidebar-content .active {
    background-color: #666; /* Warna latar belakang saat tautan aktif dipilih */
}

    </style>
    """, unsafe_allow_html=True)
