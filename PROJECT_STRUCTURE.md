# 🚀 Product Intelligence Engine - Project Overview

## 📁 Complete Project Structure

```
Product_Intellegence_Engine/
│
├── 📂 config/                          # Configuration management
│   ├── __init__.py
│   ├── config.py                       # Central configuration file
│   └── README.md                       # Config documentation
│
├── 📂 data/                            # Data storage
│   ├── raw/                            # Scraped raw reviews
│   ├── processed/                      # LLM-classified reviews
│   └── samples/                        # Sample data for testing
│       ├── README.md
│       └── sample_reviews.csv
│
├── 📂 scripts/                         # Core processing modules
│   ├── __init__.py
│   ├── scraper.py                      # Google Play Store scraper
│   ├── process_llm.py                  # LLM classifier (Gemini)
│   └── visualize.py                    # Chart generator
│
├── 📂 utils/                           # Utility functions
│   ├── __init__.py
│   ├── data_handler.py                 # CSV operations & validation
│   └── logger.py                       # Logging utilities
│
├── 📂 notebooks/                       # Jupyter notebooks
│   └── data_exploration.ipynb          # Data analysis & visualization
│
├── 📂 dashboard/                       # Dashboard & visualization
│   ├── exports/                        # Generated files (auto-created)
│   ├── README.md                       # Dashboard guide
│   ├── looker_studio_guide.md          # Looker Studio setup
│   └── sample_dashboard_config.json    # Dashboard configuration
│
├── 📄 main.py                          # Main pipeline orchestrator
├── 📄 requirements.txt                 # Python dependencies
├── 📄 .env.example                     # Environment variables template
├── 📄 .gitignore                       # Git ignore rules
├── 📄 LICENSE                          # MIT License
├── 📄 README.md                        # Main documentation
├── 📄 QUICKSTART.md                    # Quick start guide
└── 📄 TESTING.md                       # Testing guide

```

## 🎯 Key Features

### 1. **Modular Architecture**
- Separation of concerns (scraper, processor, visualizer)
- Easy to maintain and extend
- Reusable components

### 2. **Configuration Management**
- Centralized settings in `config/config.py`
- Environment-based API keys
- Easy customization

### 3. **Robust Error Handling**
- Comprehensive logging
- Retry mechanisms for API calls
- Graceful failure handling

### 4. **Data Pipeline**
- **Phase 1**: Web scraping from Google Play Store
- **Phase 2**: LLM classification with Gemini
- **Phase 3**: Analysis and insights
- **Phase 4**: Visualization and dashboard export

### 5. **Flexible Execution**
- Full pipeline mode
- Individual phase execution
- Custom parameters via CLI

### 6. **Production Ready**
- Clean code with docstrings
- Type hints
- Comprehensive logging
- Sample data for testing

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Web Scraping** | google-play-scraper |
| **AI/LLM** | Google Gemini API |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Dashboard** | Looker Studio |
| **Config** | python-dotenv |

## 📊 Data Flow

```
Google Play Store
        ↓
    [SCRAPER]
        ↓
   Raw Reviews CSV
        ↓
  [LLM PROCESSOR]
        ↓
 Classified Reviews CSV
        ↓
    [ANALYZER]
        ↓
   Insights & Stats
        ↓
   [VISUALIZER]
        ↓
Charts + Looker Data
        ↓
  Looker Studio Dashboard
```

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup environment
cp .env.example .env
# Edit .env and add GEMINI_API_KEY

# 3. Run pipeline
python main.py

# 4. Check outputs
# - data/processed/ for classified reviews
# - dashboard/exports/ for visualizations
```

## 📚 Documentation

| File | Description |
|------|-------------|
| `README.md` | Main project documentation |
| `QUICKSTART.md` | Quick start guide |
| `TESTING.md` | Testing guide |
| `config/README.md` | Configuration guide |
| `dashboard/README.md` | Dashboard setup guide |
| `dashboard/looker_studio_guide.md` | Detailed Looker Studio tutorial |

## 🎨 Output Examples

### Console Output
```
🚀 Starting Google Play Store Scraper
📱 Fetching app info for: com.unnes.myunnes
✅ App: MyUNNES | Rating: 4.2 | Reviews: 1,234
🔍 Starting to scrape reviews...
✅ Successfully scraped 1000 reviews
💾 Reviews saved to: data/raw/reviews_20251007.csv

🤖 Starting LLM Processing Pipeline
🤖 Processing 1000 reviews with LLM...
✅ Classification completed!

📊 PROCESSING SUMMARY:
   Total reviews processed: 1000
   Category Distribution:
      UI/UX: 245
      Performance: 198
      Feature: 167
   ...
```

### Generated Files
- `data/processed/processed_reviews_*.csv` - Full classified dataset
- `dashboard/exports/looker_studio_data.csv` - Dashboard-ready data
- `dashboard/exports/*.png` - Visualization charts
- `pipeline.log` - Detailed execution logs

## 🔐 Security

- API keys stored in `.env` (gitignored)
- No sensitive data in repository
- Environment-based configuration

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👨‍💻 Author

**raindragon14**
- GitHub: [@raindragon14](https://github.com/raindragon14)

## 🆘 Support

- 📖 Read the documentation
- 🧪 Check [TESTING.md](TESTING.md) for troubleshooting
- 🐛 Report issues on GitHub
- 💬 Join discussions

## 🎯 Use Cases

1. **Product Managers**: Understand user pain points
2. **Developers**: Prioritize bug fixes and features
3. **UX Designers**: Identify usability issues
4. **Marketing**: Track sentiment and satisfaction
5. **Leadership**: Data-driven product decisions

## 📈 Future Enhancements

- [ ] Multi-app comparison
- [ ] Automated scheduling
- [ ] Email reports
- [ ] Real-time monitoring
- [ ] More visualization types
- [ ] API endpoints
- [ ] Web interface

---

**Made with ❤️ for Better Product Decisions**

Last Updated: October 7, 2025
