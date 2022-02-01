from genericpath import exists
import os

from json import loads

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise

from src.config.service import Settings
from src.config.database import CONFIG

from src.service.routes.references import publications
from src.service.routes import catalogues
from src.service.routes.references import acts
from src.service.routes.references import subjects
from src.service.routes.references import working
from src.service.routes.references import organizations
from src.service.routes.references import levels


settings = Settings()

app = FastAPI(docs_url=None, redoc_url=None, debug=settings.fastapi_app_debug)

app.title = settings.fastapi_app_title
app.version = settings.fastapi_app_version
app.contact = {'author':'Rostislav Aleev', 'mail':'rs.aleev@gmail.com'}
app.description = settings.fastapi_app_title


app.state.static_folder = "./src/service/static"
app.state.temp_folder = "./src/service/temp"


app.mount("/static", StaticFiles(directory=app.state.static_folder), name='static')
app.mount("/tmp",StaticFiles(directory=app.state.temp_folder), name='temp')

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

# app.include_router(publications.router)
# app.include_router(catalogues.router)
# app.include_router(acts.router)
# app.include_router(subjects.router)
# app.include_router(working.router)
# app.include_router(levels.router)
# app.include_router(organizations.router)


# register_tortoise(
#     app,
#     config=CONFIG,
#     generate_schemas=True,
#     add_exception_handlers=False,
# )

@app.get("/health", include_in_schema=False)
async def get_status():
    # if Tortoise._inited:
    #     return 1
    # else:
    #     return 0
    return 1

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="static/swagger-ui-bundle.js",
        swagger_css_url="static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()
