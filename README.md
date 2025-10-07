<div align="center">

# 🚀 Product Intelligence Engine (PI-Engine)

### *Transforming User Feedback into Actionable Product Insights*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Gemini API](https://img.shields.io/badge/Gemini-API-orange.svg)](https://ai.google.dev/)
[![Looker Studio](https://img.shields.io/badge/Looker-Studio-green.svg)](https://lookerstudio.google.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📋 Latar Belakang

Tim produk sering menghadapi tantangan dalam mengidentifikasi inti dari keluhan pengguna dan memahami bagaimana posisi fitur produk mereka dibandingkan dengan para kompetitor. Tanpa sistem yang terstruktur, proses analisis ulasan menjadi manual, memakan waktu, dan rentan terhadap bias subjektif.

**PI-Engine** hadir sebagai solusi dengan membangun pipeline data otomatis yang mampu mengklasifikasikan umpan balik pengguna hingga ke akar masalahnya. Selain itu, sistem ini juga menyediakan dasbor visualisasi yang memudahkan tim untuk mengambil keputusan berbasis data secara cepat dan akurat.

---

## 🎯 Fitur Utama

✨ **Klasifikasi Otomatis** - Menggunakan LLM untuk mengkategorikan feedback pengguna  
📊 **Dashboard Interaktif** - Visualisasi insight dengan Looker Studio  
🔄 **Pipeline Terotomasi** - Proses ETL end-to-end tanpa intervensi manual  
🎯 **Analisis Kompetitor** - Bandingkan produk Anda dengan kompetitor  
📈 **Trend Analysis** - Identifikasi pola keluhan dari waktu ke waktu  

---

## 📊 Diagram Alur Sistem

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#4CAF50','primaryTextColor':'#fff','primaryBorderColor':'#2E7D32','lineColor':'#1976D2','secondaryColor':'#2196F3','tertiaryColor':'#FF9800','background':'#ffffff','mainBkg':'#4CAF50','secondBkg':'#2196F3','tertiaryBkg':'#FF9800','textColor':'#333333','fontSize':'16px'}}}%%
graph TD
    A["📱 Data Mentah Ulasan<br/>Google Play Store"] --> B["🔧 Script Pengumpulan Data<br/>google-play-scraper"]
    B --> C["📄 File CSV Mentah<br/>Raw Reviews"]
    C --> D["🤖 Script Pemrosesan LLM<br/>Gemini API + Pandas"]
    D --> E["📊 File CSV Terstruktur<br/>Classified Feedback"]
    E --> F["📈 Dasbor Looker Studio<br/>Visualisasi & Insight"]
    
    style A fill:#1976D2,stroke:#0D47A1,stroke-width:2px,color:#fff
    style B fill:#FF6F00,stroke:#E65100,stroke-width:2px,color:#fff
    style C fill:#7B1FA2,stroke:#4A148C,stroke-width:2px,color:#fff
    style D fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#fff
    style E fill:#C2185B,stroke:#880E4F,stroke-width:2px,color:#fff
    style F fill:#F57C00,stroke:#E65100,stroke-width:2px,color:#fff
```

### 🔄 Alur Kerja Pipeline

| Tahap | Deskripsi | Tools |
|-------|-----------|-------|
| **1. Data Collection** | Scraping ulasan dari Google Play Store | google-play-scraper |
| **2. Data Storage** | Menyimpan data mentah dalam format CSV | Pandas |
| **3. LLM Processing** | Klasifikasi dan analisis menggunakan AI | Google Gemini API |
| **4. Structured Output** | Data terstruktur dengan kategori keluhan | Pandas |
| **5. Visualization** | Dashboard interaktif untuk product insights | Matplotlib, Looker Studio |

---

## 🛠️ Tech Stack

<table>
<tr>
<td>

**Backend & Processing**
- 🐍 Python 3.8+
- 🐼 Pandas (Data manipulation)
- 🌐 google-play-scraper (Scraping)
- 📊 Matplotlib/Seaborn (Visualization)
- 📓 Jupyter Notebook (Analysis)

</td>
<td>

**AI & Cloud**
- 🤖 Google Gemini API (LLM)
- 📈 Looker Studio (Dashboard)
- 💾 CSV/JSON Storage
- 🔄 Automated ETL Pipeline
- 🔐 dotenv (Environment config)

</td>
</tr>
</table>

---

## 📈 Spesifikasi Data

| Parameter | Detail |
|-----------|--------|
| **Sumber Data** | Ulasan Google Play Store |
| **Objek Analisis** | MyUNNES |
| **Volume Data** | 800-1200 ulasan terbaru per aplikasi |
| **Update Frequency** | Otomatis/On-demand |

---

## 🚀 Cara Penggunaan

### 1️⃣ Clone Repository
```bash
git clone https://github.com/raindragon14/Product_Intellegence_Engine.git
cd Product_Intellegence_Engine
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment
```bash
# Salin file environment template
cp .env.example .env

# Edit file .env dan tambahkan API key Anda
# GEMINI_API_KEY=your-api-key-here
```

> 🔑 **Dapatkan API Key**: [Google AI Studio](https://ai.google.dev/)

### 4️⃣ Jalankan Pipeline

**Opsi 1: Jalankan Full Pipeline (Recommended)**
```bash
# Menjalankan seluruh pipeline secara otomatis
python main.py
```

**Opsi 2: Jalankan Per Tahap**
```bash
# 1. Scraping data
python scripts/scraper.py

# 2. Proses dengan LLM
python scripts/process_llm.py

# 3. Generate visualisasi
python scripts/visualize.py
```

**Opsi 3: Dengan CLI Arguments**
```bash
# Batasi jumlah review
python main.py --max-reviews 500

# Gunakan app ID berbeda
python main.py --app-id com.your.app

# Jalankan hanya scraping
python main.py --scrape-only

# Jalankan hanya visualisasi (memerlukan data processed)
python main.py --visualize-only
```

---

## 📁 Struktur Folder

```
Product_Intellegence_Engine/
├── 📂 config/                  # Konfigurasi aplikasi
│   ├── config.py              # File konfigurasi utama
│   └── README.md              # Dokumentasi konfigurasi
│
├── 📂 data/                    # Data storage
│   ├── raw/                   # Data mentah dari scraping
│   ├── processed/             # Data hasil pemrosesan LLM
│   └── samples/               # Contoh data untuk testing
│
├── 📂 scripts/                 # Core modules
│   ├── scraper.py             # Script pengumpulan data (Google Play Store)
│   ├── process_llm.py         # Script klasifikasi dengan LLM
│   └── visualize.py           # Script generasi visualisasi
│
├── 📂 utils/                   # Helper utilities
│   ├── data_handler.py        # Operasi data CSV
│   └── logger.py              # Logging utilities
│
├── 📂 notebooks/               # Jupyter notebooks
│   └── data_exploration.ipynb # Eksplorasi & analisis data
│
├── 📂 dashboard/               # Dashboard & visualisasi
│   ├── exports/               # Chart & data export (auto-generated)
│   ├── README.md              # Panduan dashboard
│   ├── looker_studio_guide.md # Tutorial Looker Studio
│   └── sample_dashboard_config.json
│
├── 📄 main.py                  # Pipeline orchestrator utama
├── 📄 requirements.txt         # Dependencies Python
├── 📄 .env.example             # Template environment variables
├── 📄 README.md                # Dokumentasi utama (file ini)
├── 📄 QUICKSTART.md            # Panduan cepat memulai
├── 📄 TESTING.md               # Panduan testing
└── 📄 PROJECT_STRUCTURE.md     # Overview struktur lengkap
```

---

## 📊 Output & Hasil

### Sample Dashboard
- 📌 **Top Complaints** - 10 keluhan teratas dari pengguna
- 📈 **Trend Analysis** - Perubahan sentimen dari waktu ke waktu
- 🎯 **Feature Comparison** - Benchmarking dengan kompetitor
- 🔍 **Root Cause Analysis** - Kategori masalah utama

### File yang Dihasilkan
```
dashboard/exports/
├── looker_studio_data.csv      # Data siap import ke Looker Studio
├── dashboard_summary.json      # Ringkasan statistik
├── category_distribution.png   # Chart distribusi kategori
├── sentiment_analysis.png      # Chart analisis sentimen
├── trend_analysis.png          # Chart trend waktu
└── priority_distribution.png   # Chart distribusi prioritas
```

### Console Output
Setelah menjalankan pipeline, Anda akan melihat:
- ✅ Statistik pengumpulan data
- 📊 Distribusi kategori & sentimen
- ⚠️ Issues dengan prioritas tinggi
- ⭐ Distribusi rating
- 🎨 Lokasi file visualisasi

---

## 📚 Dokumentasi Lengkap

| Dokumen | Deskripsi |
|---------|-----------|
| [QUICKSTART.md](QUICKSTART.md) | Panduan cepat memulai |
| [TESTING.md](TESTING.md) | Panduan testing & troubleshooting |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Overview lengkap struktur project |
| [config/README.md](config/README.md) | Dokumentasi konfigurasi |
| [dashboard/README.md](dashboard/README.md) | Setup dashboard & visualisasi |
| [dashboard/looker_studio_guide.md](dashboard/looker_studio_guide.md) | Tutorial Looker Studio detail |

---

## 🤝 Kontribusi

Kontribusi selalu terbuka! Silakan:
1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📝 Lisensi

Project ini menggunakan lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail.

---

## 👨‍💻 Author

**raindragon14**
- GitHub: [@raindragon14](https://github.com/raindragon14)

---

<div align="center">

### ⭐ Jika project ini bermanfaat, berikan bintang ya!

**Made with ❤️ for Better Product Decisions**

</div>
