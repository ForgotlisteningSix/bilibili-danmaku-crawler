# Bilibili Danmaku Crawler

## 📌 Introduction

A simple Python crawler for fetching danmaku (bullet comments) from Bilibili videos and exporting them to a CSV file for further analysis.

---

## 🚀 Features

* Fetch danmaku data in XML format
* Parse danmaku text content
* Export structured data to CSV

---

## 🛠️ Requirements

```bash
pip install requests lxml
```

---

## 📥 How to Get CID (Important)

CID (Comment ID) is the unique identifier for danmaku data.

### Normal Videos

Open Developer Tools (F12) → Network → search for `.xml`:

```
https://comment.bilibili.com/123456.xml
```

👉 `123456` is the CID

---

### Bangumi (Anime / Episodes)

Episode links (ep) cannot be used directly.

You need to find the CID from:

* `.xml` request in Network
* or `oid` parameter in API requests

👉 `oid` is essentially the CID

---

### Verification

Open in browser:

```
https://comment.bilibili.com/your_cid.xml
```

If the XML loads correctly, the CID is valid.

---

## ▶️ Usage

Modify the CID in the script:

```python
cid = 5000135
```

Run:

```bash
python parse_danmaku.py
```

---

## 📊 Output

The program generates:

```
danmaku.csv
```

Example:

| Danmaku  |
| -------- |
| hahaha   |
| incoming |
| amazing  |
| wow      |

> ⚠️ Output results depend on the selected video's danmaku content.

---

## 🧠 Workflow

```
Get CID → Request XML → Parse Data → Export CSV
```

---

## ⚠️ Disclaimer

This project is for educational and research purposes only. Please comply with Bilibili's terms of service.

---

## 👤 Author

GitHub: https://github.com/ForgotlisteningSix

