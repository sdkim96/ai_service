import logging
from pathlib import Path

from fastapi import FastAPI

from apps.exceptions import (ItemNotFoundException, NothingToRespondException, ValidationErrorException, item_not_found_exception_handler, nothing_to_respond_exception_handler, validation_error_exception_handler)
from apps.endpoint import router
# from midjourney_apis import midjourney_router

logger = logging.getLogger(__name__)

app = FastAPI()

ROOT = Path(__file__)

app.add_exception_handler(ItemNotFoundException, item_not_found_exception_handler)
app.add_exception_handler(NothingToRespondException, nothing_to_respond_exception_handler)
app.add_exception_handler(ValidationErrorException, validation_error_exception_handler)

app.include_router(router, prefix="/fastapi")

@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*")
