
import requests
from bs4 import BeautifulSoup
import json
import MakeJson

def UserInfo():

    # My Git Page Follower Info Crwaling

    resp = requests.get('https://github.com/taehyundev?tab=followers')
    soup = BeautifulSoup(resp.text, 'html.parser')
    titles = soup.select('span.link-gray')
    name = list()
    name.append('taehyundev') #My info
    url = list()
    url.append('https://github.com/taehyundev') #My info
    for title in titles:
        name.append(title.get_text())

    for i in range(1, len(name)):
        url.append('https://github.com/'+name[i])
    
    max = len(name) # 나의 팔로워수 
    print(max)
    u_info = dict()
    cnt =0
    for i in range(0, max):
        u_info[cnt] = {"name":name[i],"url":url[i]}
        cnt = cnt+1

    return MakeJson.m_json("data/userinfo.json",u_info )
UserInfo()