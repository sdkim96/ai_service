from fastapi import APIRouter, Request, Depends
from apps.exceptions import *
from starlette.concurrency import run_in_threadpool

from apps.schema import *
from apps.openais import messages, runs, threads, assistants

router = APIRouter()

class ObjectCaching():
    def __init__(self):
        self.message_client = messages.Messages()
        self.run_client = runs.Runs()
        self.thread_client = threads.Threads()
        self.assistant_client = assistants.Assistants()

    def get_message_client(self):
        return self.message_client

    def get_run_client(self):
        return self.run_client
    
    def get_thread_client(self):
        return self.thread_client
    
    def get_assistant_client(self):
        return self.assistant_client

# FastAPI 의존성 주입 시스템을 사용하여 객체 캐싱
cache = ObjectCaching()

        

    
# 1. object get방식

@router.get("/openai/get_assistant", response_model=Assistant)
async def get_assistant(assistant_id: str, assistant_client: assistants.Assistants = Depends(cache.get_assistant_client)):
    my_assistant = assistant_client.retrieve_assistant(assistant_id=assistant_id)
    if not my_assistant:
        raise HTTPException(status_code=404, detail="No assistant found for the given assistant ID.")
    return my_assistant


@router.get("/openai/get_thread", response_model=Thread)
async def get_thread(thread_id: str, thread_client: threads.Threads = Depends(cache.get_thread_client)):
    my_thread = thread_client.retrieve_thread(thread_id=thread_id)
    if not my_thread:
        raise HTTPException(status_code=404, detail="No thread found for the given thread ID.")
    return my_thread


@router.get("/openai/get_messages", response_model=List[Message])
async def get_messages(thread_id: str, message_client: messages.Messages = Depends(cache.get_message_client)):
    my_thread_messages = message_client.list_messages(thread_id=thread_id)
    if not my_thread_messages:
        raise HTTPException(status_code=404, detail="No messages found for the given thread ID.")
    return my_thread_messages


@router.get("/openai/retrieve_run", response_model=Run)
async def get_run(thread_id: str, run_id: str, run_client: runs.Runs = Depends(cache.get_run_client)):
    my_thread_run = run_client.retrieve_run(thread_id=thread_id, run_id=run_id)
    if not my_thread_run:
        raise HTTPException(status_code=404, detail="No runs found for the given thread ID.")
    return my_thread_run


@router.get("/openai/list_runs", response_model=List[Run])
async def get_runs(thread_id: str, run_client: runs.Runs = Depends(cache.get_run_client)):
    my_thread_runs = run_client.list_runs(thread_id=thread_id)
    if not my_thread_runs:
        raise HTTPException(status_code=404, detail="No runs found for the given thread ID.")
    return my_thread_runs


# 2. object post방식

@router.post("/openai/create_message", response_model=Message)
async def create_message(body: CreateMessageInput, message_client: messages.Messages = Depends(cache.get_message_client)):
    thread_message = message_client.create_message(thread_id=body.thread_id, role=body.role, content=body.content)
    if not thread_message:
        raise HTTPException(status_code=404, detail="No messages found for the given thread ID.")
    return thread_message


@router.get("/openai/create_run", response_model=Run)
async def create_run(thread_id: str, assistant_id: str, run_client: runs.Runs = Depends(cache.get_run_client)):
    run = run_client.create_run(thread_id=thread_id, assistant_id=assistant_id)
    if not run:
        raise HTTPException(status_code=404, detail="No messages found for the given thread ID.")
    return run


@router.get("/openai/create_thread", response_model=Thread)
async def create_thread(thread_client: threads.Threads = Depends(cache.get_thread_client)):
    empty_thread = thread_client.create_thread()
    if not empty_thread:
        raise HTTPException(status_code=404, detail="쓰레드 생성 실패")
    return empty_thread






@router.post("/openai/run")
async def run_gpt(prompt_data: Prompt):
    print(prompt_data)
    try:
        prompt = prompt_data.which_prompt()
        print(prompt)

        return {"message": "Received", "prompt": prompt}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))