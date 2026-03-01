from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="MJU Capstone AI AGENTI",
    description="명지대학교 자연캠퍼스 가이드 및 여행 일정을 짜주는 AI 에이전트 서버입니다.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 허용할 Origin(출처) 리스트
origins = [
    "http://localhost:8080",    # 로컬 Spring Boot 서버
    "http://127.0.0.1:8080",    # 로컬 IP 주소
]

# CORS 미들웨어 등록
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 허용할 도메인 목록
    allow_credentials=True,           # 쿠키/인증 정보 포함 허용 여부
    allow_methods=["*"],              # 모든 HTTP 메서드 허용 (GET, POST, PUT 등)
    allow_headers=["*"],              # 모든 HTTP 헤더 허용
)

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Capstone AI API is running(CORS Settings Applied!)"}
