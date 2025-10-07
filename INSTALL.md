# 🔧 Installation Troubleshooting Guide

## Error: metadata-generation-failed

Jika Anda mendapat error saat `pip install -r requirements.txt`, ikuti langkah berikut:

### ✅ SOLUSI TERCEPAT (Untuk Python 3.13)

```powershell
# Virtual environment sudah dibuat otomatis
# Langsung install packages satu per satu:

pip install python-dotenv pandas numpy requests tqdm
pip install google-play-scraper google-generativeai beautifulsoup4
pip install matplotlib seaborn openpyxl
pip install jupyter ipykernel
```

### Solusi 1: Install Bertahap

```powershell
# Install core dependencies dulu
pip install python-dotenv
pip install pandas
pip install requests
pip install google-play-scraper
pip install google-generativeai
pip install tqdm

# Lalu install visualization (optional)
pip install matplotlib
pip install seaborn
```

### Solusi 2: Gunakan Requirements Minimal

```powershell
pip install -r requirements-minimal.txt
```

### Solusi 3: Update pip, setuptools, wheel

```powershell
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

### Solusi 4: Install dengan --no-cache-dir

```powershell
pip install --no-cache-dir -r requirements.txt
```

### Solusi 5: Gunakan Virtual Environment (Recommended)

```powershell
# Buat virtual environment
python -m venv venv

# Aktifkan
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

## Masalah Spesifik per Package

### NumPy/Pandas Error

Jika error pada NumPy atau Pandas:

```powershell
# Untuk Windows, install pre-built binary
pip install --only-binary=:all: numpy pandas
```

### Matplotlib Error

Jika error pada Matplotlib:

```powershell
# Install tanpa dependencies dulu
pip install --no-deps matplotlib
pip install pillow
```

### Jupyter Error

Jika error pada Jupyter:

```powershell
# Skip Jupyter jika tidak dibutuhkan
# Atau install notebook saja
pip install notebook
```

## Versi Python yang Direkomendasikan

- ✅ Python 3.9
- ✅ Python 3.10
- ✅ Python 3.11
- ⚠️ Python 3.8 (mungkin ada masalah compatibility)
- ❌ Python 3.12 (beberapa package belum support)

Check versi Python Anda:
```powershell
python --version
```

## Install Visual C++ Build Tools (Windows)

Beberapa package memerlukan compiler C++. Download dari:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

Atau install via:
```powershell
# Jika ada chocolatey
choco install visualstudio2019buildtools
```

## Alternatif: Conda Environment

Jika masih error, coba gunakan Conda:

```powershell
# Install Miniconda: https://docs.conda.io/en/latest/miniconda.html

# Buat environment
conda create -n pi-engine python=3.10
conda activate pi-engine

# Install packages
conda install pandas numpy matplotlib seaborn jupyter
pip install python-dotenv google-play-scraper google-generativeai tqdm
```

## Test Instalasi

Setelah instalasi, test dengan:

```powershell
python -c "import pandas; import requests; import google.generativeai; print('✅ Core packages OK!')"
```

## Dependencies yang Paling Penting

Untuk menjalankan core functionality, Anda minimal perlu:

1. ✅ `python-dotenv` - Environment variables
2. ✅ `pandas` - Data processing
3. ✅ `requests` - HTTP requests
4. ✅ `google-play-scraper` - Scraping reviews
5. ✅ `google-generativeai` - LLM processing
6. ✅ `tqdm` - Progress bars

Visualization (optional):
7. ⭕ `matplotlib` - Charts
8. ⭕ `seaborn` - Statistical plots

Development (optional):
9. ⭕ `jupyter` - Notebooks
10. ⭕ `openpyxl` - Excel support

## Menjalankan Tanpa Visualization

Jika Anda skip visualization packages, Anda masih bisa:

```powershell
# Scraping
python scripts/scraper.py

# Processing
python scripts/process_llm.py

# Full pipeline (tanpa visualisasi)
python main.py --scrape-only
python main.py --process-only
```

## Bantuan Lebih Lanjut

Jika masih error, buka issue di GitHub dengan informasi:
- Versi Python: `python --version`
- Versi pip: `pip --version`
- OS: Windows/Linux/Mac
- Full error message
- Output dari: `pip list`

---

**Quick Fix (Copy-Paste)**

```powershell
# Buat virtual environment dan install minimal
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install python-dotenv pandas requests google-play-scraper google-generativeai tqdm
```

Kemudian jalankan:
```powershell
# Test
python -c "from config.config import GEMINI_API_KEY; print('Config OK!')"
```
