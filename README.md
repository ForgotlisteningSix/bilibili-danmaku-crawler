# Bilibili Danmaku Crawler

## 📌 项目简介

一个基于 Python 的弹幕爬虫工具，用于抓取哔哩哔哩（Bilibili）视频弹幕，并导出为 CSV 文件，便于后续数据分析。

---

## 🚀 功能

* 获取视频弹幕 XML 数据
* 解析弹幕文本内容
* 导出结构化 CSV 文件

---

## 🛠️ 环境依赖

```bash id="a8k2mx"
pip install requests lxml
```

---

## 📥 获取 CID（关键）

CID 是弹幕数据的唯一标识，不同视频对应不同 CID。

### 普通视频

在开发者工具（F12）→ Network 中搜索 `.xml`：

```text id="p7x2ld"
https://comment.bilibili.com/123456.xml
```

👉 `123456` 即 CID

---

### 番剧（bangumi）

番剧（ep 链接）不能直接使用，需要在 Network 中获取：

* `.xml` 请求中的 `oid` 即 CID
* 本质等同于弹幕视频 ID

---

### 验证方式

在浏览器中访问：

```text id="m9k8qv"
https://comment.bilibili.com/你的cid.xml
```

若可正常打开 XML 文件，则 CID 有效。

---

## ▶️ 使用方法

修改代码中的 CID：

```python id="v2k7zd"
cid = 5000135
```

运行程序：

```bash id="c5n2qp"
python parse_danmaku.py
```

---

## 📊 输出结果

程序运行后会生成：

```text id="t9v3mx"
danmaku.csv
```

### 示例输出：

| 弹幕内容 |
| ---- |
| 哈哈哈  |
| 前方高能 |
| 来了来了 |
| 泪目   |

> ⚠️ 输出结果基于所选视频的弹幕内容，不同视频结果会完全不同。

---

## 🧠 项目原理

```text id="q2m8ld"
获取 CID → 请求 XML → 解析弹幕 → 保存为 CSV
```

---

## ⚠️ 说明

本项目仅用于学习与数据分析研究，请遵守相关平台使用规范。

---

## 👤 作者

GitHub: https://github.com/ForgotlisteningSix

