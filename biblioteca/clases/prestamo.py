from datetime import datetime, timedelta
from auxiliares import constantes
import detalle_libro

class Prestamo(detalle_libro.DetalleLibro):
    def __init__(self, isbn, ejemplares_disponibles, fecha_prestamo, fecha_devolucion, cantidad_solicitada):
        super().__init__(self, isbn, ejemplares_disponibles)
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
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