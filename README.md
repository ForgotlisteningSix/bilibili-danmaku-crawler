# Bilibili Danmaku Analysis Toolkit

## 📌 Introduction

Bilibili Danmaku Analysis Toolkit is a Python-based toolkit for collecting, processing, and analyzing danmaku (bullet comments) from Bilibili videos.

The project supports the complete workflow from danmaku acquisition to text analysis, including:

* Automatic CID retrieval from BV IDs
* Danmaku downloading
* XML parsing
* CSV export
* Chinese word segmentation
* Stopword filtering
* Word frequency analysis
* Word cloud visualization

This toolkit was developed as a small-scale corpus analysis tool and can be applied to audience studies, digital humanities research, intercultural communication research, and social media discourse analysis.

---

## 🚀 Features

### Data Collection

* Automatically retrieve CID from Bilibili BV IDs
* Download danmaku data in XML format
* Parse danmaku content from XML files
* Export danmaku data to CSV format

### Text Analysis

* Chinese word segmentation using Jieba
* Stopword filtering
* High-frequency word statistics
* Top keyword extraction

### Visualization

* Generate word cloud visualizations
* Export word cloud images as PNG files

---

## 📂 Project Structure

```text
.
├── crawler
│   ├── get_cid.py
│   ├── fetch_danmaku.py
│   └── parse_danmaku.py
│
├── analysis
│   ├── word_freq.py
│   └── wordcloud_m.py
│
├── data
│   └── danmaku.csv
│
├── output
│   └── wordcloud.png
│
├── stopwords.txt
├── README.md
└── .gitignore
```

---

## 🛠 Requirements

Install dependencies:

```bash
pip install requests lxml pandas jieba wordcloud matplotlib
```

---

## ▶ Workflow

```text
BV ID
 ↓
Get CID
 ↓
Download Danmaku XML
 ↓
Parse XML
 ↓
Export CSV
 ↓
Chinese Word Segmentation
 ↓
Stopword Filtering
 ↓
Word Frequency Analysis
 ↓
Word Cloud Visualization
```

---

## 📥 Usage

### Step 1: Get CID from BV ID

```python
from get_cid import get_cid

cid = get_cid("BVxxxxxxxxx")
print(cid)
```

---

### Step 2: Download and Parse Danmaku

Modify the CID value in:

```python
cid = your_cid
```

Run:

```bash
python crawler/parse_danmaku.py
```

Output:

```text
data/danmaku.csv
```

---

### Step 3: Word Frequency Analysis

Run:

```bash
python analysis/word_freq.py
```

Example output:

```text
中国 532
日本 421
文化 318
纪录片 287
```

---

### Step 4: Generate Word Cloud

Run:

```bash
python analysis/wordcloud_m.py
```

Output:

```text
output/wordcloud.png
```

---

## 📊 Example Output

CSV:

| 弹幕内容     |
| -------- |
| 哈哈哈      |
| 来了来了     |
| 泪目       |
| 日本人好有礼貌  |
| 中国文化真有意思 |

Word Cloud:

```text
output/wordcloud.png
```

---

## 🔬 Research Applications

This project can be used for:

* Corpus Linguistics
* Audience Research
* Digital Humanities
* Intercultural Communication Studies
* Social Media Discourse Analysis
* Cultural Perception Research
* Online Community Studies

Example research topics:

* Audience responses to documentary films
* Cross-cultural communication on social media
* Danmaku discourse analysis
* Keyword extraction from online comments
* Public perception studies

---

## ⚠ Limitations

* Currently supports single-video danmaku collection.
* Historical danmaku retrieval is not implemented.
* Word segmentation quality depends on Jieba's dictionary.
* Chinese font paths may need adjustment on non-Windows systems.

---

## 📈 Future Improvements

* Historical danmaku support
* Sentiment analysis
* Topic modeling
* Network analysis
* Interactive visualization dashboard
* Multi-video corpus construction

---

## ⚠ Disclaimer

This project is intended for educational and research purposes only.

Users should comply with Bilibili's Terms of Service when collecting and using data.

---

## 👤 Author

GitHub: https://github.com/ForgotlisteningSix
