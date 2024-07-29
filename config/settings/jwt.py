from datetime import timedelta, datetime

from config.env import env, env_to_int
from rich import print
from rich.console import Console
import json

console = Console()

print("[bold green]CONFIGURACION EXITOSA DE JWT")
# Convierte las variables de entorno a un diccionario
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=env_to_int(env("ACCESS_TOKEN_LIFETIME"))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=env_to_int(env("ACCESS_TOKEN_LIFETIME"))),
    "ROTATE_REFRESH_TOKENS": env("ROTATE_REFRESH_TOKENS"),
    "BLACKLIST_AFTER_ROTATION": env("BLACKLIST_AFTER_ROTATION"),
    "UPDATE_LAST_LOGIN": env("UPDATE_LAST_LOGIN"),
}
