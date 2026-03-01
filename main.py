from fastapi import FastAPI

app = FastAPI(
    title="MJU Capstone AI AGENTI",
    description="명지대학교 자연캠퍼스 가이드 및 여행 일정을 짜주는 AI 에이전트 서버입니다.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
async def root():
    return {"message": "Capstone AI API is running"}
