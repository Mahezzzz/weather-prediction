import streamlit as st

st.set_page_config(
    page_title="Information Pages",
    page_icon="✨"
)
st.sidebar.write("Anda berada di Menu Informasi")

st.title("Tentang Prediksi Cuaca")
# 1. Berawan (Cloudy)
st.header("1. Berawan (Cloudy)")
st.image("berawan.png", width=200)
st.write("Pada kondisi berawan, kelembaban relatif berada dalam rentang 72% hingga 79%. Ini menunjukkan tingkat kelembaban yang cukup tinggi namun masih dalam batas normal. Curah hujan pada kondisi ini berkisar antara 0 mm hingga 7.4 mm, yang berarti bisa saja tidak ada hujan sama sekali atau hanya hujan ringan. Durasi sinar matahari yang dapat diterima bervariasi antara 0.6 hingga 6.8 jam per hari, menunjukkan adanya variabilitas dalam jumlah sinar matahari yang bisa diterima. Kecepatan angin pada kondisi berawan biasanya berada dalam rentang 2 hingga 4 km/jam.")

# 2. Hujan (Rainy)
st.header("2. Hujan (Rainy)")
st.image("hujan.png", width=200)
st.write("Pada kondisi hujan, kelembaban relatif lebih tinggi, berada dalam rentang 79% hingga 92%. Hal ini menunjukkan atmosfer yang sangat lembab. Curah hujan pada kondisi ini dapat sangat bervariasi, dari tidak ada hujan sama sekali hingga 50.9 mm, yang menunjukkan kemungkinan terjadinya hujan lebat. Durasi sinar matahari berkisar antara 0 hingga 7.7 jam per hari, yang menunjukkan bahwa meskipun hujan, masih ada kemungkinan mendapatkan sinar matahari. Kecepatan angin pada kondisi hujan biasanya lebih rendah, berada dalam rentang 1 hingga 3 km/jam.")

# 3. Cerah (Sunny)
st.header("3. Cerah (Sunny)")
st.image("cerah.png", width=200)
st.write("Pada kondisi cerah, kelembaban relatif berada dalam rentang 73% hingga 84%. Tidak ada curah hujan pada kondisi ini, dengan curah hujan 0 mm. Durasi sinar matahari sangat tinggi, berkisar antara 6.4 hingga 10.4 jam per hari, menunjukkan adanya paparan sinar matahari yang cukup lama. Kecepatan angin pada kondisi cerah biasanya berada dalam rentang 2 hingga 3 km/jam.")

# 4. Berangin (Windy)

st.header("4. Berangin (Windy)")
st.image("berangin.png", width=200)
st.write("Pada kondisi berangin, kelembaban relatif tetap pada 73%. Tidak ada curah hujan pada kondisi ini, dengan curah hujan 0 mm. Durasi sinar matahari juga cukup stabil, berkisar antara 8.1 hingga 8.2 jam per hari, menunjukkan adanya paparan sinar matahari yang cukup konsisten. Kecepatan angin pada kondisi berangin tetap pada 4 km/jam, yang menunjukkan adanya angin yang cukup signifikan namun stabil.")

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
        [data-testid="stSidebar"] {
        background: linear-gradient(#fff394,#fff9e2);
        padding: 20px;
    }
    h1 {
        color: #1a4b94; /* Warna teks judul */
    }
    h2 {
        color: #2775bf; /* Warna teks judul */
    }
    
     </style>
    """, unsafe_allow_html=True)
