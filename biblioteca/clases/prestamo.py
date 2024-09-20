from datetime import datetime, timedelta
from auxiliares import constantes
import detalle_libro
import usuario

class Prestamo(detalle_libro, usuario):
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamo, fecha_devolucion, fecha_devuelto, cantidad_solicitada):
        detalle_libro.__init__(isbn)
        usuario.__init__(id_usuario)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_devuelto
        self.cantidad_solicitada = cantidad_solicitada
    
    def sumar_dias_laborales(fecha_prestamo, dias_prestamo):
        dias_agregados = 0  
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(days=1)
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1
        return fecha_prestamo
        
    def calcular_fechas(self):
        if(self.ejemplares_disponibles > 0):
            if(self.ejemplares_disponibles > self.cantidad_solicitada):
                self.fecha_prestamo = datetime.datetime.now()
                self.fecha_devolucion = Prestamo.sumar_dias_laborales(self.fecha_prestamo, 5)