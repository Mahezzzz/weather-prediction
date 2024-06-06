import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

st.set_page_config(
    page_title="Prediction Pages",
    page_icon="✨"
)

# Memuat model cuaca yang telah dilatih sebelumnya
weather_model = joblib.load(open('weather_model.sav', 'rb'))

# Add a cloud image
st.image("cuaca 3.png", width=600)

# Judul aplikasi Streamlit
st.title('Test Prediksi Cuaca')

# Membuat dua kolom untuk bidang input
col1, col2 = st.columns(2)

# Bidang input untuk suhu, curah hujan, kelembaban, sinar UV, dan kecepatan angin
with col1:
    temp = st.text_input('Input Nilai Temperatur Rata-rata (°C)')

with col2:
    sunshine = st.text_input('Input Nilai Penyinaran Matahari (jam)')

with col1:
    humidity = st.text_input('Input Nilai Kelembapan Rata-rata (%)')

with col2:
    wind_speed = st.text_input('Input Nilai Kecepatan Angin Rata-rata (m/s)')

with col1:
    rainfall = st.text_input('Input Nilai Curah Hujan (mm)')

# Fungsi untuk memprediksi cuaca berdasarkan data input
def predict_weather(temp, humidity, rainfall, sunshine, wind_speed):
    try:
        # Memastikan semua input dikonversi ke float
        temp = float(temp)
        humidity = float(humidity)
        rainfall = float(rainfall)
        sunshine = float(sunshine)
        wind_speed = float(wind_speed)
    except ValueError:
        return "Input tidak valid. Mohon masukkan nilai numerik."
    
     # Memastikan semua input dikonversi ke int
    rainfall = int(rainfall)
    sunshine = int(sunshine)
    wind_speed = int(wind_speed)
    temp = int(temp)
    humidity = int(humidity)
    
 #Logika prediksi berdasarkan analisis data
    if humidity == 73 and rainfall == 0 and (8 <= sunshine <= 8.3) and wind_speed == 4:
        return 'Berangin'
    elif (73 <= humidity <= 84) and rainfall == 0 and (6.4 <= sunshine <= 10.4) and (2 <= wind_speed <= 3):
        return 'Cerah'
    elif (79 <= humidity <= 92) and (0 <= rainfall <= 50.9) and (0 <= sunshine <= 7.7) and (1 <= wind_speed <= 3):
        return 'Hujan'
    elif (72 <= humidity <= 79) and (0 <= rainfall <= 7.4) and (0.6 <= sunshine <= 6.8) and (2 <= wind_speed <= 4):
        return 'Berawan'
    else:
        return 'Tidak diketahui'

# Tombol untuk memicu prediksi
if st.button("Prediksi Cuaca"):
    if temp and humidity and rainfall and sunshine and wind_speed:
        prediction = predict_weather(temp, humidity, rainfall, sunshine, wind_speed)
        st.write(f"Prediksi cuaca adalah: {prediction}")
    else:
        st.write("Mohon masukkan semua nilai input.")


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
    .stButton>button {
        background-color: #499deb; /* Warna latar belakang tombol */
        color: white; /* Warna teks tombol */
        border: none; /* Hilangkan border */
        border-radius: 4px; /* Radius sudut tombol */
        padding: 10px 20px; /* Padding tombol */
        margin-top: 10px; /* Margin atas tombol */
    }
        [data-testid="stSidebar"] {
        background: linear-gradient(#fff394,#fff9e2);
        padding: 20px;.sidebar .sidebar-content {
    
    /* CSS untuk latar belakang kolom input */
    .stTextInput>div>div>div {
        background-color: #dddd; /* Warna latar belakang kolom input */
    }
    label {
    color: #101486; /* Warna teks label */
    display: block; /* Tampilkan dalam blok */
    margin-bottom: 5px; /* Margin bawah */
    }
    /* CSS untuk tombol saat dihover */
    button:hover {
    background-color: ##499de; /* Warna latar belakang tombol saat dihover */
    }
    </style>
    """, unsafe_allow_html=True)

