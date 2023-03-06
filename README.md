# Coding-test
Numble - 코딩테스트 플랫폼 구축하기 챌린지


### Project review ~~[GoTo]~~
- 프로젝트 회고록

## Task interpretation
해당 기능을 사용할 수 있는 권한이 있는 유저에게 코딩테스트 문제 풀이 기능을 제공하는 서비스라고 해석하였습니다.

## Implementation requirements

## Implementation

### Tech Stack
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white"/>

### Development Period
* 2023.03

> ### ERD

> ### API Specification ~~[GoTo]~~

> ### Implementation Process

### Step to run
> window 환경에서 구현 및 실행되었습니다.

#### Local server
1. github에서 해당 프로젝트의 repository를 clone합니다.
```shell
$ git clone https://github.com/Jjenny-K/coding-test.git
```

2. .env 파일을 root directory에 생성 후, 프로젝트와 연동을 위한 정보를 저장합니다.
```
SECRET_KEY='{SECRET_KEY}'
```

3. 가상환경을 설정한 후 필요한 라이브러리를 설치합니다.
```shell
$ python -m venv venv
$ venv\Scripts\activate
$ python install -r requirements.txt
```

4. model migration을 진행합니다.
```shell
$ python manage.py migrate
```

5. local server를 실행합니다.
```shell
$ python manage.py runserver
```

## Author
All of development : :monkey_face: **Kang Jeonghui**
