from tipo_categoria import TipoCategoria as tipo_cat

class Categoria_Libro(tipo_cat):
    def __init__(self, id_categoria_libro, id_tipo_categoria, categoria_libro):
        tipo_cat.__init__(id_tipo_categoria)
        self.id_categoria_libro = id_categoria_libro
        self.categoria_libro = categoria_libro
