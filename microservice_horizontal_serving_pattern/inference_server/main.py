import uvicorn
from fastapi import FastAPI

import api

app = FastAPI(title="test-api")

app.include_router(api.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0")