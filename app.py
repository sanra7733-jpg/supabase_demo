import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Inicializar el cliente de Supabase de forma correcta
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# SELECT * FROM contactos;
def obtenerContactos():
    # Realizar la consulta a la tabla 'contactos'
    response = supabase.table("contactos").select("*").execute()
    return response.data

# Imprimir los resultados en la terminal
print(obtenerContactos())


