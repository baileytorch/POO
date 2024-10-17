import TipoCategoria

class Categoria_Libro(TipoCategoria):
    def __init__(self, id_categoria_libro, id_tipo_categoria, categoria_libro):
        super().__init__(id_tipo_categoria)
        self.id_categoria_libro = id_categoria_libro
        self.categoria_libro = categoria_libro
