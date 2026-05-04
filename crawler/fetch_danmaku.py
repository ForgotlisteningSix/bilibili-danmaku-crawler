import requests

def fetch_danmaku(cid):
    url = f"https://comment.bilibili.com/{cid}.xml"
    
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    return response.text


if __name__ == "__main__":
    cid = 0   # ?? 先写0，等会我们再改
    
    xml_data = fetch_danmaku(cid)
    
    print(xml_data[:200])
