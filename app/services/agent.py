# LangChain Agent logic placeholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from app.core.config import settings

def get_chat_agent(session_id: str):
    # 1. Gemini LLM 설정
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0.7
    )

    # 2. Redis를 통한 대화 기록 저장소 연결
    # 자바 세션과 섞이지 않게 'message_store:' 접두사를 붙입니다.
    chat_history = RedisChatMessageHistory(
        url=settings.REDIS_URL,
        session_id=session_id,
        key_prefix="message_store:"
    )

    # 3. 요약형 버퍼 메모리 설정
    # max_token_limit을 넘어가면 LLM이 이전 대화를 요약해서 저장합니다.
    memory = ConversationSummaryBufferMemory(
        llm=llm,
        chat_memory=chat_history,
        max_token_limit=1000, # 약 1000토큰이 넘어가면 요약 시작
        return_messages=True,
        memory_key="chat_history"
    )

    return llm, memory