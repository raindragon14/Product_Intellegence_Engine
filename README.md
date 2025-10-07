# Product_Intellegence_Engine

Tim produk sering menghadapi tantangan dalam mengidentifikasi inti dari keluhan pengguna dan memahami bagaimana posisi fitur produk mereka dibandingkan dengan para kompetitor. Tanpa sistem yang terstr[...]

PI-Engine hadir sebagai solusi dengan membangun pipeline data otomatis yang mampu mengklasifikasikan umpan balik pengguna hingga ke akar masalahnya. Selain itu, sistem ini juga menyediakan dasbor visu[...]

Sumber Data: Ulasan Google Play Store.
Objek Analisis: MyUNNES.
Volume Data: 800-1200 ulasan terbaru per aplikasi.

--Tech Stack--
Bahasa Pemrograman: Python
Library: Pandas, Requests/Scrapy, Matplotlib/Seaborn.
LLM API: Google AI (Gemini API).
Visualisasi: Looker Studio (gratis)

## 📊 Diagram Alur Sistem

```
┌─────────────────────────────┐
│   Data Mentah (Ulasan)      │
│   Google Play Store         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Script Pengumpulan Data     │
│ (Requests/Scrapy)           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   File CSV Mentah           │
│   (Raw Reviews)             │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Script Pemrosesan LLM       │
│ (Gemini API + Pandas)       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  File CSV Terstruktur       │
│  (Classified Feedback)      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Dasbor Looker Studio      │
│   (Visualisasi & Insight)   │
└─────────────────────────────┘
```

**Alur Kerja:**
1. **Data Collection** - Scraping ulasan dari Google Play Store
2. **Data Storage** - Menyimpan data mentah dalam format CSV
3. **LLM Processing** - Klasifikasi dan analisis menggunakan Gemini API
4. **Structured Output** - Data terstruktur dengan kategori keluhan
5. **Visualization** - Dashboard interaktif untuk product insights
