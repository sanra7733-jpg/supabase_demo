import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:

    def GET(self):
        model_contactos = ModelContactos()
        
        return render.index()

