import pytest
from sqlalchemy import text
from redis.asyncio import Redis
from app.core.config import settings
from app.core.database import AsyncSessionLocal

async def test_supabase_connection():
    """Supabase(DB) 연결 테스트"""
    async with AsyncSessionLocal() as session:
        # SELECT 1 쿼리로 DB 생존 확인
        result = await session.execute(text("SELECT 1"))
        assert result.scalar() == 1
        print("\n[DB] Supabase 연결 성공!")

async def test_upstash_redis_connection():
    """Upstash(Redis) 연결 테스트"""
    # .env의 REDIS_URL로 접속
    redis_client = Redis.from_url(settings.REDIS_URL)
    
    # PING 날리기
    ping_response = await redis_client.ping()
    assert ping_response is True
    print("\n[Redis] Upstash 연결 성공!")
    
    await redis_client.aclose()