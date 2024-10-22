def consulta_1():
    consulta1 = (f"""
    SELECT
        L.isbn 'ISBN', 
        L.titulo 'Título', 
        A.seudonimo_autor 'Seudónimo', 
        P.gentilicio_pais 'Nacionalidad', 
        E.nombre_editorial 'Editorial', 
        IF(D.fecha_edicion, DATE_FORMAT(D.fecha_edicion, '%d/%m/%Y'), 'Desconocido') 'Fecha Edición', 
        CONCAT(T.tipo_categoria, '-', C.categoria_libro) 'Categoría Libro', 
        IFNULL(NULLIF(D.numero_paginas, 0), 'No Especificado') 'Cantidad Páginas', 
        D.ejemplares_disponibles 'Cantidad Disponible' 
    FROM  libro L 
    JOIN autor A ON L.id_autor = A.id_autor 
    JOIN paises P ON A.codigo_pais = P.codigo_pais 
    JOIN detalle_libro D ON L.isbn = D.isbn 
    JOIN editorial E ON D.id_editorial = E.id_editorial 
    JOIN categoria_libro C ON D.id_categoria_libro = C.id_categoria_libro 
    JOIN tipo_categoria T ON C.id_tipo_categoria = T.id_tipo_categoria;
    """)
    return consulta1

def consulta_3(seudonimo):
    consulta_3 = (f"""SELECT * FROM AUTOR WHERE seudonimo_autor LIKE '%{seudonimo}%'""")
    return consulta_3