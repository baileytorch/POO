import re
from paises import Pais as pais

class Editorial():
    def __init__(self, id_editorial, nombre_editorial, fecha_fundacion, codigo_pais, telefono_contacto, correo_contacto):
        pais.__init__(codigo_pais)
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial
        self.fecha_fundacion = fecha_fundacion
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
    
    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo_usuario)):
            return True 
        else:
            return False