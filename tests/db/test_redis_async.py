import pytest
from redis.asyncio import Redis
from app.core.config import settings

@pytest.mark.asyncio
async def test_upstash_redis_connection():
    """Upstash(Redis) 연결 테스트 (비동기 방식)"""
    # .env의 REDIS_URL로 접속
    redis_client = Redis.from_url(settings.REDIS_URL)
    
    try:
        # PING 날리기
        ping_response = await redis_client.ping()
        assert ping_response is True
        print("\n[Redis] Upstash 연결 성공!")
    finally:
        await redis_client.aclose()
