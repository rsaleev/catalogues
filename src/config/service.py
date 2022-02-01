
from typing import Dict, List, Any, Optional
from pydantic import BaseSettings, validator

""""
https://pydantic-docs.helpmanual.io/usage/settings/
"""

class Settings(BaseSettings):

    fastapi_app_debug: bool = True
    fastapi_app_title:Optional[str] = 'FastAPI'
    fastapi_app_version:Optional[str] = '0.1.0'
    cors_allow_methods: Optional[List[str]] = ["*"]
    cors_allow_origins: Optional[List[str]] = ["*"]
    cors_allow_credentials: Optional[bool] = True
    cors_allow_headers: Optional[List[str]]= ["*"]

    class Config:
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(
            cls,
            env_settings,
            init_settings,
            
        ):
            return (
                env_settings,
                init_settings,
            )
