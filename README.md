# POO

Clases, Objetos e información relativa a POO en proyecto Biblioteca

Para conectar DB instalamos y usamos XAMPP con Apache y MySQL
https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html

Para conectar a DB usamos mysql-coonector-python
Ejecutar en terminal:
pip install mysql-connector-python

Para usar un ORM, tenemos una buena opción en orm-mysql:
https://pypi.org/project/orm-mysql/

Para validación de RUT, usamos rut-chile
https://pypi.org/project/rut-chile/
Ejecutar en terminal: pip install rut_chile
Uso:
from rut_chile import rut_chile

        rut_chile.is_valid_rut("12345678-9")
        # returns False
        rut_chile.is_valid_rut("6265837-1")
        # returns True

        # Formatos soportados

        rut_chile.is_valid_rut("98685030")
        # returns True
        rut_chile.is_valid_rut("9868503-0")
        # returns True
        rut_chile.is_valid_rut("9.868.503-0")
        # returns True
        rut_chile.is_valid_rut("12.667.869-K")
        # returns True
        rut_chile.is_valid_rut("12.667.869-k")
        # returns True

Para entorno gráfico: https://youtu.be/vNw-zLB7GLY
Para navegación y acciones: https://youtu.be/LNQcnbqBh4k

Pillow para trabajar con imágenes: pip install Pillow==11.0.0

bootstrap: https://ttkbootstrap.readthedocs.io/en/version-0.5/index.html
Para cambiar temas: https://youtu.be/OPyRdmMQYOA

CRUD: https://youtu.be/UdIx9g5X1wQ
