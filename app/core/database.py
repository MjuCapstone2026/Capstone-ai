# Database configuration placeholder
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
from sqlalchemy.pool import NullPool

# 1. 비동기 DB 엔진 생성
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    poolclass=NullPool, 
    connect_args={
        "statement_cache_size": 0,       # 캐시 끄기
        "prepared_statement_cache_size": 0 # 캐시 끄기 (asyncpg 전용)
    }
)

# 2. 비동기 세션 생성기 (자바의 EntityManagerFactory 역할)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 3. 모델(Entity)의 베이스 클래스
Base = declarative_base()

# 4. 의존성 주입(Dependency Injection)을 위한 함수
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()