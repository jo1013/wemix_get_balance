# wemix_get_balance

### app/constants/token_addresses.py
  * 토큰주소는 변경해줘야한다.

### docker build -t get_balance .

#### dockerfile이 있는 폴더에서 실행
docker build -t get_balance .
docker run -p 8000:8000 get_balance


예: /balance/0xYourAddress/wemix?timestamp=2023-09-30 12:00:00

timestamp를 지정하지 않으면 최신 블록의 잔액을 반환합니다.

## 토큰 주소들 (wemix chain)

    WEMIX = ""
    WWEMIX = "0x7D72b22a74A216Af4a002a1095C8C707d6eC1C5f"
    WEMIX_DOLLAR = "0x8E81fCc2d4A3bAa0eE9044E0D7E36F59C9BbA9c1"
    WCD = "0x2ec6Fc5c495aF0C439E17268d595286d5f897dD0"
    VEL = "0x1BABB9d9a013533Fa48BA874580AFD7bEA9278EF"
    SOUL = "0x5bB4a218CFaa191Ba05C5f1036f2d4a1e04600e5"
    KLAY = "0x461d52769884ca6235B685EF2040F47d30C94EB5"
    USDC = "0xE3F5a90F9cb311505cd691a46596599aA1A0AD7D"
    ETH = "0x765277EebeCA2e31912C9946eAe1021199B39C61"
    BNB = "0xC1Be9a4D5D45BeeACAE296a7BD5fADBfc14602C4"
    KLEVA = "0xe6801928061CDbE32AC5AD0634427E140EFd05F9"
    USDT = "0xA649325Aa7C5093d12D6F98EB4378deAe68CE23F"
    oUSDC = "0xE4c2b5db9de5da0A17ED7ec7176602ad99E52624"   



## 구조

```
/fastapi_project
│
├── /app
│   ├── __init__.py
│   ├── main.py                # FastAPI 앱 인스턴스와 라우터들을 포함하는 메인 파일
│   ├── /models
│   │   ├── __init__.py
│   │   ├── item.py           # Pydantic 모델과 같은 데이터 모델
│   │   └── user.py
│   │
│   ├── /routers
│   │   ├── __init__.py
│   │   ├── item_router.py    # 각각의 엔드포인트 및 비즈니스 로직을 포함하는 라우터
│   │   └── user_router.py
│   │
│   └── /dependencies
│       ├── __init__.py
│       └── database.py       # 데이터베이스 연결 및 다른 종속성
│   └── /constants                # 상수를 보관하기 위한 디렉토리
│       ├── __init__.py
│       └── token_addresses.py   # ENUM으로 토큰 주소를 관리하는 파일
├── /tests
│   ├── __init__.py
│   ├── test_main.py          # 테스트 케이스
│   └── ...
│   └── /resources              # 리소스를 보관하기 위한 디렉토리
│       └── token_abi.json      # 토큰의 ABI를 포함하는 JSON 파일
├── Dockerfile                # 앱을 Docker 컨테이너로 실행하기 위한 Dockerfile
├── requirements.txt          # 필요한 Python 패키지를 나열하는 파일
└── .gitignore
```