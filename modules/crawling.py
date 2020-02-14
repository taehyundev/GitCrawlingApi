import json
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import MakeJson

def Crawling_git():
    #현재 날짜
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')

    #날짜 정하기
    #date = "2020-02-13"
    m_data = dict()

    # 전체 내용 빼기
    with open('data/userinfo.json', 'r',encoding='utf-8') as f:
        info = json.load(f)

    #반복문으로 json 데이터 받기
    name =list()
    url =list()
    for i in range(0, len(info)):
        name.append(info[str(i)]["name"])
        url.append(info[str(i)]["url"])
    cnt =0
    #Git 커밋 크롤링
    print("Wait! plz~")
    for i in range(0, len(info)):
        html = urllib.request.urlopen(url[i]).read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all(class_='day')
        for j in title:
            if (j["data-date"] == date):
                m_data[str(cnt)] = {"name":name[i],"commit-count":j["data-count"]}
                cnt = cnt +1
    #json 파일로 만드는 모듈
    return MakeJson.m_json("data/commit_result.json",m_data)
    
Crawling_git()
