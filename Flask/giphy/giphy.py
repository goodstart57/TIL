from datetime import datetime
from pprint import pprint as pp
import requests
import os

def join_giphy_url(query, n=5):
    base_url = "http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit={}".format(query, os.environ["gp_key"], n)
    return base_url
    
def get_trending_url(n=25):
    base_url = "http://api.giphy.com/v1/gifs/trending?api_key={}&limit={}".format(os.environ["gp_key"], n)
    return base_url
    
def send_request(base_url):
    res = requests.get(base_url)
    return res

def get_img_urls_in_giphy_res(gres):
    return list(map(lambda x: x['images']['original']['url'], gres.json()['data']))

def get_iurls_titles_ratings_link_from_res(gres):
    """
    Get 
    title -- title name
    gurl -- gif url
    rating -- rating
    glink -- giphy link
    olink -- original post link
    """
    infos = gres.json()['data']
    titles = list(map(lambda x: x['title'], infos))
    gurls = list(map(lambda x: x['images']['original']['url'], infos))
    ratings = list(map(lambda x: x['rating'], infos))
    glinks = list(map(lambda x: x['url'], infos))
    olinks = list(map(lambda x: x['source_post_url'], infos))
    info = []
    for t, gu, r, g, o in zip(titles, gurls, ratings, glinks, olinks):
        info_dict = {}
        info_dict["title"] = t
        info_dict["gurl"] = gu
        info_dict["rating"] = r
        info_dict["glink"] = g
        info_dict["olink"] = o
        info.append(info_dict)
    return info

def save_gif(url, filename):
    with open('./images/{}_{}.gif'.format(filename, datetime.now().strftime("%Y%m%d%H%M%s%f")), 'wb') as f:
        f.write(requests.get(url).content)

if __name__=="__main__":
    keyword = input("검색할 짤의 키워드를 입력해주세요 : ")
    base_url = join_giphy_url(keyword)
    res = send_request(base_url)
    if res.status_code//100 == 2:
        urls = get_img_urls_in_giphy_res(res)
        for url in urls:
            save_gif(url, keyword)
    else:
        print("Please Input Correct Query")
    
