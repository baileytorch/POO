import detalle_libro
import biblioteca
import usuario

class Devolucion(detalle_libro.DetalleLibro, usuario.Usuario):
    def __init__(self, isbn, id_usuario, fecha_devuelto, cantidad):
        detalle_libro.DetalleLibro.__init__(self, isbn)
        usuario.Usuario.__init__(self, id_usuario)
        self.fecha_devuelto = fecha_devuelto
        self.cantidad = cantidad