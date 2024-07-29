# Esta clase se encarga de crear una instancia de environ para poder ser llamado en todos los archivos de configuracion
# de igual manera se encarga de definir la ruta de las aplicaciones

import environ
from rich import print

env = environ.Env()
BASE_DIR = environ.Path(__file__) - 2  # - 2 niveles de directorios para llegar a la raiz
APPS_DIR = BASE_DIR('core')

print("[bold green]DIRECTORIO BASE Y DIRECTORIO APPS")
print(f"[red]{BASE_DIR}")
print(f"[red]{APPS_DIR}")


# transforma una variable de entorno en numero
def env_to_int(value):
    return int(value)
