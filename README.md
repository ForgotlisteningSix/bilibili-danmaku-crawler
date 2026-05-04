# Bilibili Danmaku Crawler

## 📌 项目简介

一个基于 Python 的简单爬虫工具，用于抓取哔哩哔哩视频弹幕，并导出为 CSV 文件，便于后续数据分析。

---

## 🚀 功能

* 获取视频弹幕 XML 数据
* 解析弹幕文本
* 导出 CSV 文件

---

## 🛠️ 环境依赖

```bash
pip install requests lxml
```

---

## 📥 获取 CID（关键）

CID 是弹幕数据的唯一标识。

### 普通视频

打开浏览器开发者工具（F12）→ Network，搜索 `.xml`：

```
https://comment.bilibili.com/123456.xml
```

👉 `123456` 即 CID

---

### 番剧（bangumi）

番剧链接（ep）不能直接使用，需要在 Network 中获取：

* `.xml` 请求
* 或接口中的 `oid`（即 CID）

---

### 验证

在浏览器打开：

```
https://comment.bilibili.com/你的cid.xml
```

能访问即为有效 CID

---

## ▶️ 使用方法

修改代码中的 CID：

```python
cid = 5000135
```

运行：

```bash
python parse_danmaku.py
```

---

## 📊 输出结果

生成文件：

```
danmaku.csv
```

终端示例输出：

```
哈哈哈哈
来了来了
前方高能
这波可以
```

---

## 🧠 项目原理

```
获取CID → 请求XML → 解析弹幕 → 保存CSV
```

---

## ⚠️ 说明

本项目仅用于学习交流，请遵守相关平台规则。

---

## 👤 作者

https://github.com/ForgotlistenSix

