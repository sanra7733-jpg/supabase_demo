import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")
    
    # SELECT * FROM contactos;
    def obtenerContactos(self):
        # Corregido: se usa 'self.supabase' para acceder al cliente inicializado en __init__
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self,id_contacto:int):
        response = self.supabase.table("contactos").select("*").eq("id_contacto",id_contacto).execute()
        return response.data
    
    def insertarContacto(self, nombre:str, email:str, telefono:str):
        nuevo_contacto = {
            "nombre":nombre,
            "email":email,
            "telefono":telefono
        }
        response = self.supabase.table("contactos").insert(nuevo_contacto).execute()
        return response.data

    def borrarContacto(self, id_contacto:int):
        response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()

    def actualizarContacto(self,id_contacto:int, nombre:str, email:str, telefono:str):
        datos_actualizados = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").update(datos_actualizados).eq("id_contacto", id_contacto).execute()
        return response.data
                                       
if __name__ == "__main__":
# Ejecución de prueba
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(1))
    print(model_contactos.insertarContacto("jose","jose@gmail.com", "112345378"))
    print(model_contactos.borrarContacto(1))
    print(model_contactos.actualizarContacto(1, "Dejah Thors", "deja@gmail.com", "99999999"))
