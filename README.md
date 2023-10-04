# wemix_get_balance

이 프로젝트는 WEMIX 체인의 토큰 및 ETH 잔액을 조회하는 FastAPI 기반 웹 애플리케이션입니다.

## 토큰 주소 변경

토큰 주소를 변경하려면 `app/constants/token_addresses.py` 파일에서 관련 주소를 수정하십시오.

```
# app/constants/token_addresses.py
ex ) wemixchain
WWEMIX
WEMIX_DOLLAR
WCD
VEL
SOUL
KLAY
USDC
ETH
BNB
KLEVA
USDT
oUSDC
```


## 실행 방법

Docker를 사용하여 프로젝트를 실행할 수 있습니다.

```bash
# Docker 이미지 빌드
docker build -t get_balance .

# Docker 컨테이너 실행
docker run -p 8000:8000 get_balance
```

### API 사용 예

```
GET /balance/0xYourAddress/wemix?timestamp=2023-09-30T12:00:00
```
timestamp: 지정하지 않으면 최신 블록의 잔액을 반환합니다.

### 프로젝트 구조
```
/fastapi_project
│
├── /app
│   ├── __init__.py
│   ├── main.py
│   ├── /models
│   │   ├── item.py
│   │   └── user.py
│   ├── /routers
│   │   ├── item_router.py
│   │   └── user_router.py
│   ├── /dependencies
│   │   └── database.py
│   └── /constants
│       └── token_addresses.py
├── /tests
│   ├── test_main.py
│   └── ...
├── /resources
│   └── token_abi.json
├── Dockerfile
├── requirements.txt
└── .gitignore
```