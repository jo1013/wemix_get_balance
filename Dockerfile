# 사용할 기본 이미지 선택
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일들을 컨테이너 내로 복사
COPY ./app/requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 파일들을 컨테이너 내로 복사
COPY ./app/ .

# 애플리케이션 실행 명령
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
