CREATE TABLE IF NOT EXISTS biblioteca (
    id_biblioteca INT NOT NULL AUTO_INCREMENT,
    nombre_biblioteca VARCHAR(255) NOT NULL,
    direccion_biblioteca VARCHAR(255) NULL,
    telefono_biblioteca VARCHAR(15) NULL,
    PRIMARY KEY (id_biblioteca));

CREATE TABLE IF NOT EXISTS tipo_usuario (
    id_tipo_usuario TINYINT NOT NULL AUTO_INCREMENT,
    tipo_usuario VARCHAR(50) NOT NULL,
    descripcion_tipo_usuario VARCHAR(255) NULL,
    PRIMARY KEY (id_tipo_usuario));

CREATE TABLE IF NOT EXISTS paises (
    codigo_pais INT NOT NULL,
    codigo_iso3_pais VARCHAR(3) NULL,
    nombre_pais VARCHAR(50) NOT NULL,
    gentilicio_pais VARCHAR(50) NULL,
    PRIMARY KEY (codigo_pais));

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre_usuario VARCHAR(255) NOT NULL,
    correo_usuario VARCHAR(255) NOT NULL,
    telefono_usuario VARCHAR(15) NULL,
    rut_usuario VARCHAR(10) NULL,
    codigo_pais INT NULL,
    habilitado TINYINT NOT NULL,
    id_tipo_usuario TINYINT NOT NULL,
    fecha_creacion DATETIME NOT NULL,
    contrasena VARCHAR(255) NULL,
    PRIMARY KEY (id_usuario),
    CONSTRAINT fk_pais_usuario FOREIGN KEY (codigo_pais) REFERENCES paises(codigo_pais),
    CONSTRAINT fk_tipo_usuario FOREIGN KEY (id_tipo_usuario) REFERENCES tipo_usuario(id_tipo_usuario));

CREATE TABLE IF NOT EXISTS autor (
    id_autor INT NOT NULL AUTO_INCREMENT,
    nombre_autor VARCHAR(255) NULL,
    seudonimo_autor VARCHAR(50) NOT NULL,
    codigo_pais INT NULL,
    fecha_nac DATE NULL,
    fecha_def DATE NULL,
    biografia_autor TEXT NULL,
    foto_autor BLOB NULL,
    PRIMARY KEY (id_autor),
    CONSTRAINT fk_pais_autor FOREIGN KEY (codigo_pais) REFERENCES paises(codigo_pais));

CREATE TABLE IF NOT EXISTS libro (
    isbn VARCHAR(13) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    id_autor INT,
    PRIMARY KEY (isbn),
    CONSTRAINT fk_autor_libro FOREIGN KEY (id_autor) REFERENCES autor(id_autor));

CREATE TABLE IF NOT EXISTS tipo_categoria (
    id_tipo_categoria TINYINT NOT NULL AUTO_INCREMENT,
    tipo_categoria VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_tipo_categoria));

CREATE TABLE IF NOT EXISTS categoria_libro (
    id_categoria_libro INT NOT NULL AUTO_INCREMENT,
    id_tipo_categoria TINYINT NOT NULL,
    categoria_libro VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NULL,
    PRIMARY KEY (id_categoria_libro),
    CONSTRAINT fk_tipo_categoria FOREIGN KEY (id_tipo_categoria) REFERENCES tipo_categoria(id_tipo_categoria));

CREATE TABLE IF NOT EXISTS editorial (
    id_editorial INT NOT NULL AUTO_INCREMENT,
    nombre_editorial VARCHAR(255) NOT NULL,
    fecha_fundacion DATE NULL,
    codigo_pais INT NULL,
    telefono_contacto VARCHAR(15) NULL,
    correo_contacto VARCHAR(255) NULL,
    PRIMARY KEY (id_editorial),
    CONSTRAINT fk_pais_editorial FOREIGN KEY (codigo_pais) REFERENCES paises(codigo_pais));

CREATE TABLE IF NOT EXISTS detalle_libro (
    id_detalle_libro INT NOT NULL AUTO_INCREMENT,
    isbn VARCHAR(13) NOT NULL,
    fecha_edicion DATE NULL,
    id_editorial INT NOT NULL,
    numero_paginas SMALLINT NULL DEFAULT 0,
    id_categoria_libro VARCHAR(255) NULL,
    cantidad_ejemplares SMALLINT NOT NULL,
    ejemplares_disponibles SMALLINT NOT NULL,
    PRIMARY KEY (id_detalle_libro),
    CONSTRAINT fk_isbn_libro FOREIGN KEY (isbn) REFERENCES libro(isbn),
    CONSTRAINT fk_id_editorial_libro FOREIGN KEY (id_editorial) REFERENCES editorial(id_editorial));

CREATE TABLE IF NOT EXISTS prestamo (
    id_prestamo INT NOT NULL AUTO_INCREMENT,
    id_detalle_libro INT NOT NULL,
    id_usuario INT NOT NULL,
    fecha_prestamo DATETIME NOT NULL,
    fecha_devolucion DATETIME NOT NULL,
    fecha_devuelto DATETIME NULL,
    cantidad_solicitada TINYINT NULL,
    PRIMARY KEY (id_prestamo),
    CONSTRAINT fk_detalle_libro_prestamo FOREIGN KEY (id_detalle_libro) REFERENCES detalle_libro(id_detalle_libro),
    CONSTRAINT fk_usuario_prestamo FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario));