import os

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise

from src.service.routes import publication
from src.service.routes import catalogues
from src.service.routes import acts


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(publication.router)
app.include_router(catalogues.router)
app.include_router(acts.router)

register_tortoise(
    app,
    config_file=f"{os.getcwd()}/src/config/database.json",
    generate_schemas=True,
    add_exception_handlers=False,
)

@app.get("/health")
async def get_status():
    if Tortoise._inited:
        return {"status": "ok"}
    else:
        return {"status": "error"}



