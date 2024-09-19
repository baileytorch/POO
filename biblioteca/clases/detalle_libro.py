import libro

class DetalleLibro(libro):
    def __init__(self, isbn, titulo, id_autor, numero_paginas, categoria, cantidad_ejemplares, ejemplares_disponibles):
        super().__init__(isbn, titulo, id_autor)
        self.numero_paginas = numero_paginas
        self.categoria = categoria
        self.cantidad_ejemplares = cantidad_ejemplares
        self.ejemplares_disponibles = ejemplares_disponibles
    
    def actualizar_disponibilidad(self, origen, cantidad):        
        if(self.cantidad_ejemplares > self.ejemplares_disponibles + cantidad):
            if(origen == "retirar"):
                if(self.ejemplares_disponibles > 0):
                    self.ejemplares_disponibles = self.ejemplares_disponibles - cantidad
                else:
                    print("No hay ejemplares disponibles para realizar el préstamo.")
            else:
                self.ejemplares_disponibles = self.ejemplares_disponibles + cantidad
        else:
            print("Nuestros registros indican que hay un error en la cantidad de ejemplares.")