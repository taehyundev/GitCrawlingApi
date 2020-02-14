# GitCrawlingApi
Flask와 json을 이용해서 Github commit수를 클롤링하는 Api를 만들어보자(start :2020-02-13~ )

- 127.0.0.1:5000/Commit_result 에 접속 했을 때 화면
![image](https://user-images.githubusercontent.com/50985723/74415322-801a1a80-4e86-11ea-9656-e97a088875fc.png)

# Function

#### modules 폴더에서는 MakeJson이 json 파일을 만드는 역할을 한다. ###

#### userinfo같은 경우에는 데이터를 뽑을 사용자와 url 명단을 json파일로 변환시켜서 data에 userinfo.json이라는 이름으로 저장된다. ###

#### crawling같은 경우에는 깃허브 사이트의 commit갯수를 날짜에 맞게 크롤링하여 commit_result.json이라는 파일 이름으로 저장된다. ###

       * 두개의 모듈 전부 MakeJson을 통해서 값을 json파일로 변환 시켰다.

**/commit_update : 커밋내용 업데이트 (참고 이미지)**
![image](https://user-images.githubusercontent.com/50985723/74518675-9d6ae980-4f57-11ea-93da-b432ef281bd9.png)

**/commit_result : 커밋결과 보기**

**/api/commimt : api 값 반환**
