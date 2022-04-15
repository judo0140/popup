# popup
## 0. 서비스 계정 만들기 및 dialogflow 사용하기

### 0-1. 서비스 계정 만들기
cloud.google.com 접속

우측 상단 '콘솔' 클릭

![image](https://user-images.githubusercontent.com/61779427/162685440-b05d9b60-11ad-4e26-b082-8a7ea47a1a3b.png)

약관 동의 및 계속하기

좌측 메뉴 'IAM 및 관리자' > '서비스 계정' 클릭

프로젝트 만들기 클릭

프로젝트 이름 설정 popup-346822

서비스 계정 만들기

![image](https://user-images.githubusercontent.com/61779427/162685985-ff68436c-1675-498a-a77d-beed2f5dd7a0.png)

ex)
계정이름 judo
계정ID judo-527
이메일주소 judo-527@popup-346822.iam.gserviceaccount.com
역할 소유자

![image](https://user-images.githubusercontent.com/61779427/162686324-f20c9eab-c6ad-473a-98cf-3dacdf7678ce.png)

![image](https://user-images.githubusercontent.com/61779427/162686367-d74af1e0-1b93-4c3b-8e69-20cd1d62a776.png)

키 관리 > 키 추가 > 새 키 만들기 > json 유형 선택 > 만들기

json 형태 key 파일 다운로드
(json 파일을 사용하고자 하는 메인 PC로 복사)

### 0-2. dialogflow agent 생성 및 intents 생성

dialogflow.google.com 접속

agent name 설정 및 google project >> 생성해둔 프로젝트 클릭 >> create

![image](https://user-images.githubusercontent.com/61779427/162688124-8a296504-e36a-41f7-bc08-e1b9873dd57b.png)

![image](https://user-images.githubusercontent.com/61779427/162688276-e10492ff-392b-4d10-a531-a4763b36bbbc.png)

![image](https://user-images.githubusercontent.com/61779427/162688310-39515084-ab3b-4bf6-a53e-d0ac8f02f79f.png)

intents : topic으로 보내고 싶은 의도명
Tranining Phrases : 인식하고자 하는 음성

![image](https://user-images.githubusercontent.com/61779427/162688464-eb62ff2f-cf3c-4d31-b9e2-5bef946f62b5.png)

save 클릭

### 0-3. 서비스 계정 json key 

사용하고자 하는 메인 PC에서 json key 파일 적용

~/catkin_ws/pop_up_space/scripts/real_time_test.py
~/catkin_ws/pop_up_space/scripts/pub_dialogflow.py

![image](https://user-images.githubusercontent.com/61779427/163499413-118a1a6e-6ff6-4b36-b826-747d143e8ee8.png)

노란 박스 부분의 project id, json 파일 위치 변경

![스크린샷  2022-04-11 16-55-06](https://user-images.githubusercontent.com/61779427/162693571-9d5e739f-3f20-42fd-af2e-b4d0d702aac2.png)

링크 접속

![스크린샷  2022-04-11 16-56-38](https://user-images.githubusercontent.com/61779427/162693822-23af11ea-1ae2-47ed-b654-f0c856389ee1.png)

사용 > 결제 계정 설정하기 > 설정 이후 사용


------------------
## 1. 조작 메뉴얼

### 1-0. 체크사항
* 메인 PC 및 라즈베리파이의 ROS 네트워크 설정
* 동일 네트워크망 접속 여부
* ssh 원격 접속을 위한 각 디바이스 ip address 파악
* OpenCR 보드와 12V/5A 파워 연결 여부 및 보드 내 스위치 ON/OFF 여부

![image](https://user-images.githubusercontent.com/61779427/163494820-5c9eb4d1-39b6-4751-ae93-5390ebf87e68.png)


### 1-1. 메인 PC
터미널 실행 (Ctrl + Alt + T) 후 ROS 실행
```
roscore
```

새 터미널 창 실행
(실행 이후 자동으로 음성인식이 되기에 가장 마지막에 실행 추천)
```
rosrun pop_up_space real_time_test.py
```

### 1-2. popup_pi_1 (침대, 사이드테이블 측면 라즈베리파이)

메인 PC 에서 터미널 실행 (ssh 원격 접속 + pw는 kist)
```
ssh pi@192.168.0.14
```
원격 접속 이후 노드 실행
```
rosrun popup popup_dxl_v2.py
```
노드 실행 이전에 반드시 침대, 사이드 테이블은 다 펴진 상태


### 1-3. popup_pi_2 (의자, 책상 측면 라즈베리파이)

메인 PC 에서 터미널 실행 (ssh 원격 접속 + pw는 kist)
```
ssh pi@192.168.0.11
```
원격 접속 이후 노드 실행
```
rosrun popup popup_dxl_v2.py
```
노드 실행 이전에 반드시 의자, 책상은 다 펴진 상태


### 1-4. dialogflow 없이 구동시키기 (PC에서 수동으로 topic 전송)

(roscore가 동작한다는 전제 하에)
메인 PC 에서 터미널 실행
```
rostopic pub -1 /popup_mode std_msgs/String "b1:1:1:1"
```
"b1:1:1:1" 안의 내용만 원하는 수치를 기입할 것

----------------
## 2. 소프트웨어 구성

### 2-1. Dialogflow intents

dialogflow에서 설정하는 intents가 라즈베리파이에 전송되는 ROS topic 메세지가 됨
ex) intents = "bed open" 일 경우 PC에서 라즈베리파이로 전송되는 topic은 "bed open" 이 됨

침대(1, 0.5, 0):사이드테이블(1, 0):의자(1, 0):책상(1, 0) 형태로 intents 설정
ex)
침대 전부 나옴 / 사이드테이블 들어감 / 의자 들어감 / 책상 들어감 >> intents = "b1:0:0:0"
침대 절반 나옴 / 사이드테이블 나옴 / 의자 들어감 / 책상 나옴 >> intents = "b0.5:1:0:1"

Dialogflow intents 설정은 상단 '0. 서비스 계정 만들기 및 dialogflow 사용하기' 참고

### 2-2. 각 코드 설명

코드 파일 내부의 주석 

### 2-3. OpenCR 펌웨어

본 시스템에서 OpenCR은 라즈베리파이를 이용하여 다이나믹셀 구동을 위한 usb2dxl 역할을 하기에 이에 맞는 펌웨어가 업로드 되어있어야 함

아두이노IDE 설치 : https://emanual.robotis.com/docs/en/parts/controller/opencr10/#install-on-linux
OpenCR 보드에 다이나믹셀 컨트롤을 위한 펌웨어 업로드 (OpenCR을 u2d2처럼 사용)
1) OpenCR 보드를 아두이노 IDE 실행시킬 메인 보드에 연결
2) 아두이노IDE 실행
3) Tool -> Port -> /dev/ttyACM0 (혹은 ttyUSB0.. 혹은 PC 환경마다 상이) 선택
4) File -> Examples -> OpenCR -> 10.Etc -> usb_to_dxl 클릭
5) 업로드

### 2-4. 다이나믹셀 다중 컨트롤을 위한 ID 변경

OpenCR 보드에 ID 변경하고자 하는 다이나믹셀 연결
(OpenCR은 아두이노IDE를 실행시키는 PC와 연결)

1) 아두이노IDE 실행
2) Tool -> Port -> /dev/ttyACM0 (혹은 ttyUSB0.. 혹은 PC 환경마다 상이) 선택
3) File -> Examples ->

------------------
## 3. 하드웨어 구성

### 3-1. 다이나믹셀 및 OpenCR

다이나믹셀 XM540-W270-R/T 사용
구매 : https://www.robotis.com/shop/list.php?ca_id=202020
사양 및 메뉴얼 : https://emanual.robotis.com/docs/kr/dxl/x/xm540-w270/

OpenCR
구매 : https://www.robotis.com/shop/item.php?it_id=903-0257-000

### 3-2. 프로파일 및 볼트, 너트, 브라켓

디바이스마트 메이커 서비스 활용
링크 : https://www.devicemart.co.kr/goods/maker?custom=al_profile
(원하는 규격으로 선택하여 구매)

### 3-3. 와이어 릴, 릴 커버 모델링 파일

CAD 폴더 
