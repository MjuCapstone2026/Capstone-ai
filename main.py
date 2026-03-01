from fastapi import FastAPI

app = FastAPI(title="MJU Capstone AI AGENT")

@app.get("/")
async def root():
    return {"message": "Capstone AI API is running"}
