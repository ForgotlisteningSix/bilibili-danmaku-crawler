import requests
from lxml import etree
import csv

def fetch_xml(cid):
    url = f"https://comment.bilibili.com/{cid}.xml"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.bilibili.com/"
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    
    return response.text


def parse_danmaku(xml_data):
    try:
        root = etree.fromstring(xml_data.encode('utf-8'))
    except Exception:
        print("❌ XML解析失败")
        return []
    
    danmakus = []
    
    for d in root.xpath('//d'):
        if d.text:
            danmakus.append(d.text)
    
    return danmakus


def save_to_csv(danmakus):
    with open("danmaku.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["弹幕内容"])
        
        for d in danmakus:
            writer.writerow([d])


if __name__ == "__main__":
    cid = 5000135
    
    print("正在获取弹幕数据...")
    
    xml_data = fetch_xml(cid)
    danmakus = parse_danmaku(xml_data)
    
    if danmakus:
        print("\n前20条弹幕：\n")
        
        for i, d in enumerate(danmakus[:20]):
            print(f"{i+1}. {d}")
        
        save_to_csv(danmakus)
        print("\n✅ 已保存为 danmaku.csv")
    
    else:
        print("\n❌ 没有解析到弹幕")