import streamlit as st
import pandas as pd
import numpy as np
import pickle
from urllib.parse import quote

# Olist logo (SVG) for header and favicon
olist_logo = """
<svg xmlns="http://www.w3.org/2000/svg" width="78" height="36" viewBox="0 0 548 259" fill="none">
    <g clip-path="url(#clip0)">
        <path d="M543.62 141.96H508.82L508.69 190.64C508.69 214.05 528.66 218.81 543.81 219.44C545.8 219.52 547.35 221.18 547.35 223.17V254.7C547.35 256.82 545.61 258.49 543.49 258.44C517.26 257.81 495.42 250.72 482.4 237.34C464.17 218.61 464.59 197.21 464.73 195.33L465.12 60.77C465.12 58.71 466.8 57.05 468.85 57.05H505.38C507.45 57.05 509.13 58.74 509.11 60.81L508.8 105.05H543.6C545.66 105.05 547.33 106.72 547.33 108.79V138.23C547.33 140.29 545.66 141.96 543.6 141.96" fill="white"/>
        <path d="M223.66 248.88L223.76 37.2C223.76 35.14 222.09 33.46 220.03 33.46H183.43C181.37 33.46 179.7 35.13 179.7 37.19V248.87C179.7 250.93 181.37 252.6 183.43 252.6H219.93C221.99 252.6 223.66 250.93 223.66 248.87" fill="white"/>
        <path d="M419.09 166.17C407.89 161.96 393.03 158.78 379.89 156.63C373.39 155.48 368.19 153.81 364.45 151.65C358.04 148.38 357.95 138.25 364.27 134.57C371.45 129.7 388.97 130.15 396.38 135.62C399.22 137.3 401.49 140.38 403.12 144.06C403.67 145.3 405.04 145.94 406.33 145.55L439.3 135.51C441.5 134.84 442.55 132.37 441.56 130.29C437.41 121.5 430.95 114.03 422.13 108.13C400.6 92.6 356.19 92.82 335.58 108.93C317.12 120.84 312.52 153.44 326.79 170.25C338.86 184.65 358.33 189.81 377.2 193.79C377.39 193.83 385.6 195.11 404.06 201.15C411.07 205.33 410.34 215.03 403.61 219.54C399.84 222.33 393.74 223.74 385.49 223.74C369.54 223.72 358.88 217.92 354.07 204.51C353.62 203.25 352.19 202.49 350.9 202.82L317.68 211.42C315.63 211.95 314.41 214.09 315.03 216.12C318.76 228.22 325.98 238.25 336.55 245.31C372.07 269.16 451.28 263.04 450.12 207.15C450.12 196.25 447.26 187.42 441.61 180.92C436.08 174.56 428.5 169.6 419.08 166.18" fill="white"/>
        <path d="M250.06 102.86V248.88C250.06 250.94 251.73 252.61 253.79 252.61H290.93C292.99 252.61 294.66 250.94 294.66 248.88V102.86C294.66 100.8 292.99 99.13 290.93 99.13H253.79C251.73 99.13 250.06 100.8 250.06 102.86Z" fill="white"/>
        <path d="M272.36 48.59C258.94 48.59 248.07 37.71 248.07 24.3V49.95C248.07 63.37 258.95 74.24 272.36 74.24C285.77 74.24 296.65 63.36 296.65 49.95V24.3C296.65 37.72 285.77 48.59 272.36 48.59Z" fill="#E64E36"/>
        <path d="M272.36 48.59C285.78 48.59 296.65 37.71 296.65 24.3C296.65 10.89 285.78 0 272.36 0C258.94 0 248.07 10.88 248.07 24.29C248.07 37.71 258.95 48.58 272.36 48.58" fill="white"/>
        <path d="M81.07 217.29C57.97 217.29 41.2 200.41 41.2 177.14C41.2 154.38 57.97 137.86 81.07 137.86C104.17 137.86 120.63 154.38 120.63 177.14C120.63 199.9 103.99 217.29 81.07 217.29ZM80.91 96.66C36.23 96.66 0 132.89 0 177.57C0 222.25 36.23 258.48 80.91 258.48C125.59 258.48 161.82 222.25 161.82 177.57C161.82 132.89 125.59 96.65 80.91 96.65" fill="white"/>
    </g>
    <defs>
        <clipPath id="clip0"><rect width="547.35" height="258.49" fill="white"/></clipPath>
    </defs>
</svg>
"""

olist_favicon = f"data:image/svg+xml,{quote(olist_logo.strip())}"

# Page config
st.set_page_config(
    page_title="Seller Packing Time Predictor - Olist",
    page_icon=olist_favicon,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Font Awesome for icons
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """,
    unsafe_allow_html=True,
)

# CSS - Olist branding (blue)
st.markdown(
    """
    <style>
    :root {
        --olist-primary: #003B66; /* dark blue */
        --olist-blue: #0066CC;    /* brand blue */
        --olist-light: #E8F0FF;
        --neutral: #95a5a6;
        --success: #27AE60;
        --warning: #F39C12;
        --danger:  #E74C3C;
    }

    .stApp { background-color: #FFFFFF; }

    h1, h2, h3 { color: var(--olist-primary); font-weight: 700; }

    .olist-header {
        background: linear-gradient(135deg, var(--olist-primary) 0%, var(--olist-blue) 100%);
        padding: 30px; color: #fff; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(0,59,102,.15);
    }

    .olist-header h1 { color: #fff; margin: 0; font-size: 32px; }
    .olist-header p  { margin: 8px 0; font-size: 14px; opacity: .95; }

    .input-section { background:#fff; padding:24px; border-radius:10px; border:1px solid var(--olist-light); box-shadow:0 2px 8px rgba(0,59,102,.08); margin: 16px 0; }
    .section-title { color: var(--olist-primary); font-weight: 600; font-size: 18px; border-bottom: 2px solid var(--olist-blue); padding-bottom: 10px; margin-bottom: 18px; }

    .stButton>button { width:100%; background: linear-gradient(135deg, var(--olist-primary), var(--olist-blue)) !important; color:#fff !important; font-weight:600 !important; border:none !important; border-radius:8px !important; padding:12px 20px !important; box-shadow:0 4px 12px rgba(0,59,102,.2) !important; }
    .stButton>button:hover { box-shadow:0 6px 16px rgba(0,59,102,.3) !important; transform: translateY(-1px); }

    .metric-box { background:#fff; padding:20px; border:1px solid var(--olist-light); border-radius:10px; text-align:center; box-shadow:0 2px 6px rgba(0,59,102,.08); }
    .metric-label { color: var(--neutral); font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:.4px; margin-bottom:6px; }
    .metric-value { color: var(--olist-primary); font-size:32px; font-weight:700; }
    .metric-unit  { color: var(--neutral); font-size:12px; margin-top:4px; }

    .prediction-box { background: linear-gradient(135deg, var(--olist-primary), var(--olist-blue)); color:#fff; padding:36px; border-radius:12px; text-align:center; box-shadow:0 8px 20px rgba(0,59,102,.2); margin: 20px 0; }
    .prediction-value { font-size:52px; font-weight:700; margin:14px 0; text-shadow: 0 2px 4px rgba(0,0,0,.1); }

    .risk-safe    { background:#d4edda; border-left:5px solid var(--success);  padding:16px; border-radius:8px; }
    .risk-warning { background:#fff3cd; border-left:5px solid var(--warning); padding:16px; border-radius:8px; }
    .risk-danger  { background:#f8d7da; border-left:5px solid var(--danger);  padding:16px; border-radius:8px; }

    .streamlit-expanderHeader { background-color: var(--olist-light) !important; border:1px solid #CDE0FF !important; border-radius:8px !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Model loading
@st.cache_resource
def load_model():
    with open('seller_packing_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('feature_names.pkl', 'rb') as f:
        features = pickle.load(f)
    with open('model_metrics.pkl', 'rb') as f:
        metrics = pickle.load(f)
    return model, features, metrics

try:
    model, feature_cols, metrics = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.info("Jalankan cell 'Save Model' di notebook terlebih dahulu.")
    st.stop()

# Header banner
header_html = f"""<div class='olist-header'>
<div style='display:flex;align-items:center;gap:12px;'>
{olist_logo}
<h1>Seller Packing Time Predictor</h1>
</div>
<p><i class='fas fa-chart-line'></i> Prediksi waktu packing order berdasarkan karakteristik order dan histori seller</p>
<p><i class='fas fa-brain'></i> Gunakan model machine learning untuk mengidentifikasi potensi keterlambatan dan optimalisasi performa</p>
</div>"""
st.markdown(header_html, unsafe_allow_html=True)

# Performance metrics
with st.expander("Model Performance Metrics", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            """
            <div class='metric-box'>
                <div class='metric-label'><i class=\"fas fa-calculator\"></i> RMSE</div>
                <div class='metric-value'>2.29</div>
                <div class='metric-unit'>days</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class='metric-box'>
                <div class='metric-label'><i class=\"fas fa-chart-bar\"></i> MAE</div>
                <div class='metric-value'>1.39</div>
                <div class='metric-unit'>days</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class='metric-box'>
                <div class='metric-label'><i class=\"fas fa-percent\"></i> MAPE</div>
                <div class='metric-value'>8.3%</div>
                <div class='metric-unit'>error rate</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            """
            <div class='metric-box'>
                <div class='metric-label'><i class=\"fas fa-chart-pie\"></i> R² Score</div>
                <div class='metric-value'>44.3%</div>
                <div class='metric-unit'>explained var</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# Inputs
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><i class='fas fa-edit'></i> Input Order Details</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("##### <i class='fas fa-clock'></i> Waktu Order", unsafe_allow_html=True)
    purchase_hour = st.slider("Jam order (0-23)", 0, 23, 12)
    purchase_dayofweek = st.selectbox("Hari order", [0,1,2,3,4,5,6], format_func=lambda x: ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu'][x])
    purchase_month = st.selectbox("Bulan order", list(range(1,13)), format_func=lambda x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][x-1])
    is_weekend = 1 if purchase_dayofweek in [5,6] else 0

with c2:
    st.markdown("##### <i class='fas fa-tag'></i> Detail Produk", unsafe_allow_html=True)
    price = st.number_input("Harga produk (R$)", min_value=0.0, value=100.0, step=10.0)
    freight_value = st.number_input("Biaya pengiriman (R$)", min_value=0.0, value=20.0, step=5.0)

with c3:
    st.markdown("##### <i class='fas fa-map-marker-alt'></i> Lokasi Pengiriman", unsafe_allow_html=True)
    distance_km = st.number_input("Jarak pengiriman (km)", min_value=0.0, value=500.0, step=50.0)
    is_inter_state = st.selectbox("Tipe pengiriman", [0,1], format_func=lambda x: "Dalam State" if x==0 else "Antar State")

st.markdown("</div>", unsafe_allow_html=True)

# Seller history
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><i class='fas fa-history'></i> Histori Seller</div>", unsafe_allow_html=True)
sc1, sc2, sc3, sc4, sc5 = st.columns(5)
with sc1:
    seller_avg_packing = st.number_input("Avg Packing", min_value=0.0, value=2.0, step=0.5, label_visibility="collapsed")
    st.caption("Avg packing (hari)")
with sc2:
    seller_std_packing = st.number_input("Std Packing", min_value=0.0, value=1.0, step=0.1, label_visibility="collapsed")
    st.caption("Std packing (hari)")
with sc3:
    seller_order_count = st.number_input("Order Count", min_value=1, value=50, step=10, label_visibility="collapsed")
    st.caption("Jumlah order")
with sc4:
    seller_avg_price = st.number_input("Avg Price", min_value=0.0, value=150.0, step=10.0, label_visibility="collapsed")
    st.caption("Avg price (R$)")
with sc5:
    seller_avg_freight = st.number_input("Avg Freight", min_value=0.0, value=25.0, step=5.0, label_visibility="collapsed")
    st.caption("Avg freight (R$)")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Prediction
pc1, pc2 = st.columns([2,1])
with pc1:
    input_data = pd.DataFrame({
        'price':[price],
        'freight_value':[freight_value],
        'purchase_hour':[purchase_hour],
        'purchase_dayofweek':[purchase_dayofweek],
        'purchase_month':[purchase_month],
        'is_weekend':[is_weekend],
        'seller_avg_packing':[seller_avg_packing],
        'seller_std_packing':[seller_std_packing],
        'seller_order_count':[seller_order_count],
        'distance_km':[distance_km],
        'is_inter_state':[is_inter_state],
    })

    if st.button("Prediksi Packing Time", use_container_width=True):
        pred = float(model.predict(input_data)[0])
        st.markdown(
            f"""
            <div class='prediction-box'>
                <div><i class='fas fa-hourglass-end'></i> Estimasi Waktu Packing</div>
                <div class='prediction-value'>{pred:.2f}</div>
                <div>Hari</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Risk box (no emojis)
        if pred < 1:
            risk_class, risk_level, risk_icon = "risk-safe", "SANGAT CEPAT", "<i class='fas fa-check-circle'></i>"
            advice = "Excellent! Packing time sangat optimal."
        elif pred < 2:
            risk_class, risk_level, risk_icon = "risk-safe", "CEPAT", "<i class='fas fa-check-circle'></i>"
            advice = "Good performance! Seller efisien."
        elif pred < 3:
            risk_class, risk_level, risk_icon = "risk-warning", "NORMAL", "<i class='fas fa-info-circle'></i>"
            advice = "Dalam range normal. Monitor konsistensi."
        elif pred < 5:
            risk_class, risk_level, risk_icon = "risk-warning", "LAMBAT", "<i class='fas fa-exclamation-triangle'></i>"
            advice = "Seller cenderung lambat. Berikan timeline realistis."
        else:
            risk_class, risk_level, risk_icon = "risk-danger", "SANGAT LAMBAT", "<i class='fas fa-times-circle'></i>"
            advice = "High risk! Pertimbangkan intervensi operasional."

        st.markdown(
            f"""
            <div class='{risk_class}'>
                <h4 style='margin:0 0 8px 0;'>{risk_icon} {risk_level}</h4>
                <p style='margin:0; font-size:14px;'>{advice}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Summary table
        st.markdown("### Ringkasan Input")
        summary_df = pd.DataFrame({
            'Parameter':["Waktu Order","Hari Order","Bulan Order","Harga Produk","Biaya Pengiriman","Jarak Pengiriman","Tipe Pengiriman","Seller Avg Packing","Seller Order Count"],
            'Nilai':[f"{purchase_hour:02d}:00", ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu'][purchase_dayofweek], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][purchase_month-1], f"R$ {price:.2f}", f"R$ {freight_value:.2f}", f"{distance_km:.0f} km", "Dalam State" if is_inter_state==0 else "Antar State", f"{seller_avg_packing:.2f} hari", f"{seller_order_count} order"]
        })
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

# Info expanders
ic1, ic2 = st.columns(2)
with ic1:
    with st.expander("Cara Menggunakan"):
        st.markdown(
            """
            1. Isi waktu order
            2. Masukkan detail produk
            3. Input lokasi pengiriman
            4. Lengkapi histori seller
            5. Klik tombol prediksi
            """
        )
with ic2:
    with st.expander("Model Information"):
        st.markdown(
            """
            - Algorithm: XGBoost Regressor
            - RMSE: 2.29 hari, MAE: 1.39 hari, MAPE: 8.3%, R²: 44.3%
            - Features: waktu, produk, seller history, geolocation
            """
        )

st.markdown(
    """
    <div style='text-align:center;color:#7f8c8d;margin-top:30px;padding-top:16px;border-top:1px solid #E8F0FF;'>
        <strong>Seller Performance Prediction System</strong><br/>
        Built with Alphateam Dede, Wendy and Grace
    </div>
    """,
    unsafe_allow_html=True,
)
