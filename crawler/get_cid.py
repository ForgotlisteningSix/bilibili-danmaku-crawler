import requests

def get_cid(bvid):
    url = f"https://api.bilibili.com/x/player/pagelist?bvid={bvid}"
    response = requests.get(url)
    data = response.json()
    return data['data'][0]['cid']

if __name__ == "__main__":
    cid = get_cid("BV1xx411c7mD")
    print("CIDÊÇ£º", cid)
