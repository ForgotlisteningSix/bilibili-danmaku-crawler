import requests
import csv
import os
from lxml import etree


def fetch_danmaku(cid):
    url = f"https://comment.bilibili.com/{cid}.xml"
    print("🌐 请求:", url)

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    print("📡 状态码:", response.status_code)

    if response.status_code != 200:
        print("❌ 请求失败")
        print("返回内容前100字符：", response.text[:100])
        return None

    return response.text


def parse_danmaku(xml_text):
    root = etree.fromstring(xml_text.encode("utf-8"))
    danmakus = root.xpath("//d/text()")
    return danmakus


def save_to_csv(danmakus):
    os.makedirs("data", exist_ok=True)

    path = "data/danmaku.csv"

    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["danmaku"])

        for d in danmakus:
            writer.writerow([d])

    print("✅ 已保存:", path)


def main():
    cid = 5000135  # 👉 改这里

    print("🚀 开始爬取弹幕")

    xml_text = fetch_danmaku(cid)

    danmakus = parse_danmaku(xml_text)

    print(f"📊 弹幕数量: {len(danmakus)}")

    if not danmakus:
        print("⚠️ 没有弹幕，请检查CID")
        return

    save_to_csv(danmakus)


if __name__ == "__main__":
    main()