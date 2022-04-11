# popup

cloud.google.com 접속

우측 상단 '콘솔' 클릭

![image](https://user-images.githubusercontent.com/61779427/162685440-b05d9b60-11ad-4e26-b082-8a7ea47a1a3b.png)

약관 동의 및 계속하기

좌측 메뉴 'IAM 및 관리자' > '서비스 계정' 클릭

프로젝트 만들기 클릭

프로젝트 이름 설정 popup-346822

서비스 계정 만들기

![image](https://user-images.githubusercontent.com/61779427/162685985-ff68436c-1675-498a-a77d-beed2f5dd7a0.png)

계정이름 judo
계정ID judo-527
이메일주소 judo-527@popup-346822.iam.gserviceaccount.com
역할 소유자

![image](https://user-images.githubusercontent.com/61779427/162686324-f20c9eab-c6ad-473a-98cf-3dacdf7678ce.png)

![image](https://user-images.githubusercontent.com/61779427/162686367-d74af1e0-1b93-4c3b-8e69-20cd1d62a776.png)

키 관리 > 키 추가 > 새 키 만들기 > json 유형 선택 > 만들기

json 형태 key 파일 다운로드
(json 파일을 사용하고자 하는 메인 PC로 복사)


dialogflow.google.com 접속

agent name 설정 및 google project >> 생성해둔 프로젝트 클릭 >> create

![image](https://user-images.githubusercontent.com/61779427/162688124-8a296504-e36a-41f7-bc08-e1b9873dd57b.png)

![image](https://user-images.githubusercontent.com/61779427/162688276-e10492ff-392b-4d10-a531-a4763b36bbbc.png)

![image](https://user-images.githubusercontent.com/61779427/162688310-39515084-ab3b-4bf6-a53e-d0ac8f02f79f.png)

intents : topic으로 보내고 싶은 의도명
Tranining Phrases : 인식하고자 하는 음성

![image](https://user-images.githubusercontent.com/61779427/162688464-eb62ff2f-cf3c-4d31-b9e2-5bef946f62b5.png)

save 클릭


사용하고자 하는 메인 PC에서 json key 파일 적용

~/catkin_ws/pop_up_space/scripts/real_time_test.py
~/catkin_ws/pop_up_space/scripts/pub_dialogflow.py

에서 project id, json 파일 위치 변경

![스크린샷  2022-04-11 16-55-06](https://user-images.githubusercontent.com/61779427/162693571-9d5e739f-3f20-42fd-af2e-b4d0d702aac2.png)

링크 접속

![스크린샷  2022-04-11 16-56-38](https://user-images.githubusercontent.com/61779427/162693822-23af11ea-1ae2-47ed-b654-f0c856389ee1.png)

사용 > 결제 계정 설정하기 > 설정 이후 사용
