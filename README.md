# Seller Packing Time Predictor - Olist E-Commerce

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

> **Final Project - Purwadhika Digital Technology School**

Aplikasi machine learning untuk memprediksi waktu packing seller berdasarkan karakteristik order dan histori performa seller pada platform e-commerce Olist Brazil.

## Project Overview

### Business Problem
Keterlambatan pengiriman merupakan salah satu masalah utama dalam e-commerce yang dapat menurunkan kepuasan pelanggan. Salah satu faktor penyebabnya adalah **waktu packing yang tidak konsisten** dari seller.

### Solution
Membangun model prediktif untuk memperkirakan waktu packing seller sehingga:
- Platform dapat memberikan estimasi pengiriman yang lebih akurat
- Mengidentifikasi seller dengan risiko keterlambatan tinggi
- Optimalisasi operasional dan manajemen ekspektasi customer

## Dataset

Dataset yang digunakan adalah **Brazilian E-Commerce Public Dataset by Olist** dari Kaggle yang mencakup ~100k transaksi dari 2016-2018.

**Source:** [Kaggle - Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Model Performance

| Metric | Value |
|--------|-------|
| **RMSE** | 2.29 days |
| **MAE** | 1.39 days |
| **MAPE** | 8.3% |
| **R² Score** | 44.3% |

## Tech Stack

- **Language:** Python 3.9+
- **ML Framework:** XGBoost
- **Web App:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn

## Project Structure

```
 finalproject/
├── 📄 streamlit_app.py          # Main Streamlit application
├── 📄 notebook.ipynb            # Jupyter notebook (EDA & Modeling)
├── 📄 seller_packing_model.pkl  # Trained XGBoost model
├── 📄 feature_names.pkl         # Feature names for model
├── 📄 model_metrics.pkl         # Model evaluation metrics
├── 📄 requirements.txt          # Python dependencies
└── 📄 README.md                 # Project documentation
```

## Installation & Usage

### Local Development

1. **Clone repository**
   ```bash
   git clone https://github.com/naeyanika/finalproject.git
   cd finalproject
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open browser**
   ```
   http://localhost:8501
   ```

### Streamlit Cloud Deployment

App ini dapat diakses langsung melalui Streamlit Cloud: https://finalproject-alpha.streamlit.app/

## Features

### Input Parameters

| Category | Features |
|----------|----------|
| **Waktu Order** | Jam, Hari, Bulan, Weekend/Weekday |
| **Detail Produk** | Harga, Biaya Pengiriman |
| **Lokasi** | Jarak (km), Dalam/Antar State |
| **Histori Seller** | Avg Packing Time, Std Packing, Order Count, Avg Price, Avg Freight |

### Output

-  **Prediksi Packing Time** (dalam hari)
-  **Risk Level Assessment** (Sangat Cepat → Sangat Lambat)
-  **Actionable Recommendations**

##  Requirements

```txt
streamlit
pandas
numpy
scikit-learn
xgboost
```

##  Author

**[Dede]**
**[Wendy]**
**[Grace]**

- Purwadhika Digital Technology School
- Data Science & Machine Learning Program

## License

This project is for educational purposes as part of Purwadhika Final Project.

---

<div align="center">
  <strong>Built with using Streamlit & XGBoost</strong>
  <br>
  <em>Purwadhika Digital Technology School - 2026</em>
</div>
