from pathlib import Path
import json

from typing import Dict, List, Any, Optional
from pydantic import BaseSettings, validator

""""
https://pydantic-docs.helpmanual.io/usage/settings/
"""

def json_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    """
    A simple settings source that loads variables from a JSON file
    at the project's root.

    Here we happen to choose to use the `env_file_encoding` from Config
    when reading `config.json`
    """
    encoding = settings.__config__.env_file_encoding

    return json.loads(Path(f'./src/config/service.json').read_text(encoding))

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
            file_secret_settings,
            init_settings,
            
        ):
            return (
                json_config_settings_source,
                env_settings,
                file_secret_settings,
                init_settings,
            )
