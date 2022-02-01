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
                "schema":"public"
            }
        },
        "references": {
            "engine":"tortoise.backends.asyncpg",
            "credentials":{
                "user":os.environ['DB_USER'],
                "password": os.environ['DB_PASSWORD'],
                "host":os.environ['DB_HOST'],
                "port":os.environ['DB_PORT'],
                "database": "references",
                "schema":"public"
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
                "schema":"public"
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