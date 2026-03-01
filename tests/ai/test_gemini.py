import pytest
from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

async def test_gemini_check():
    """랭체인을 이용한 Gemini 연결 최종 테스트"""
    
    # 랭체인의 Gemini 인터페이스 객체 생성
    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=1.0
    )
    
    try:
        # 랭체인 표준 메서드 ainvoke 사용
        response = await llm.ainvoke("안녕! 잘 연결되어 있어?")
        
        print(f"\n[Gemini 응답]: {response.content}")
        assert response.content is not None
        
    except Exception as e:
        print(f"\n에러 발생 상세: {e}")
        pytest.fail(f"연결 실패: {e}")