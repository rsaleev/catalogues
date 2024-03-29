from json import loads,dumps

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend


from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise

from src.config.service import Settings
from src.config.database import CONFIG

from src.service.routes.catalogues import router as r_catalogues

from src.service.routes.references.publications import router as r_publications
from src.service.routes.references.acts import router as r_acts
from src.service.routes.references.subjects import router as r_subjects
from src.service.routes.references.working import router as r_working
from src.service.routes.references.organizations import router as r_organizations
from src.service.routes.references.control import router as r_control
from src.service.routes.references.regulation import router as r_regulation
from src.service.routes.references.evaluation import router as r_evaluation
from src.service.routes.references.validity import router as r_validity

settings = Settings()

app = FastAPI(docs_url=None, redoc_url=None, debug=settings.fastapi_app_debug, root_path='/catalogues')

app.title = settings.fastapi_app_title
app.version = settings.fastapi_app_version
app.contact = settings.fastapi_app_author
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

app.include_router(r_catalogues)

app.include_router(r_acts, prefix='/references')
app.include_router(r_subjects, prefix='/references')
app.include_router(r_working, prefix='/references')
app.include_router(r_control, prefix='/references')
app.include_router(r_organizations, prefix='/references')
app.include_router(r_publications, prefix='/references')
app.include_router(r_regulation, prefix='/references')
app.include_router(r_evaluation, prefix='/references')
app.include_router(r_validity, prefix='/references')



register_tortoise(
    app,
    config=CONFIG,
    generate_schemas=False,
    add_exception_handlers=False,
)

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi_cache")


@app.get("/api/health", include_in_schema=False)
async def get_status():
    if Tortoise._inited:
        return 1
    else:
        return 0

@app.get("/api/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

