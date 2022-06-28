import uvicorn
from fastapi import FastAPI

from api import api
from configurations import APIConfigurations
from db.initialize import initialize_table
from db.database import engine

initialize_table(engine=engine, checkfirst=True)

app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    verion=APIConfigurations.version
)

app.include_router(api.router, prefix=f"/v{APIConfigurations.version}/api", tags=["api"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0")