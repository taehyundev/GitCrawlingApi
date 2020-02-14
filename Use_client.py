import requests

response = requests.get('http://127.0.0.1:5000/commit_result')
info = response.json()

for i in range(0, len(info)):
    print(str(i+1)+"번째 : "+info[str(i)]["name"] + "님의 커밋 정보 : "+info[str(i)]["commit-count"] + " commit(s)" )
