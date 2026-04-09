import functions_framework
from src.adapters.entrypoint import cloud_handler

# Este es el nombre de la función que debes poner en la consola de GCP: 'main_handler'
@functions_framework.cloud_event
def main(cloud_event):
    """
    Punto de ejecución invocado por el Functions Framework.
    Simplemente delega al adaptador de entrada.
    """
    return cloud_handler(cloud_event)