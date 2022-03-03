import os 

CONFIG = {
    "connections": {
        "ervk": {
            "engine":"tortoise.backends.asyncpg",
            "credentials": {
                "user": os.environ['DB_USER'],
                "password": os.environ['DB_PASSWORD'],
                "host":os.environ['DB_HOST'],
                "port":os.environ['DB_PORT'],
                "database": "ervk",
                "schema":"public",
                "ssl":False
            }
        },
        "references": {
            "engine":"tortoise.backends.asyncpg",
            "credentials":{
                "user":os.environ['DB_USER'],
                "password": os.environ['DB_PASSWORD'],
                "host":os.environ['DB_HOST'],
                "port":os.environ['DB_PORT'],
                "database": "reference",
                "schema":"public",
                "ssl":False
            }
        },
        "okved": {
            "engine":"tortoise.backends.asyncpg",
            "credentials":{
                "user":os.environ['DB_USER'],
                "password":os.environ['DB_PASSWORD'],
                "host":os.environ['DB_HOST'],
                "port":os.environ['DB_PORT'],
                "database":"okved",
                "schema":"public",
                "ssl":False
            }
        }
    },
    "apps": {
        "references":{
            "models": ["src.database.models.references"],
            "default_connection":"references"
        },
        "okved":{
            "models": ["src.database.models.okved"],
            "default_connection":"okved"
        },
        "ervk":{
            "models": ["src.database.models.ervk"],
            "default_connection":"ervk"
        }
    },
    "use_tz": False,
    "timezone": "Europe/Moscow"
    }