USE 4theword_prueba_andres_torres;

-- Insertar Categorías de Leyendas
INSERT INTO categorias (name)
VALUES ('Mitos'),
    ('Leyendas urbanas'),
    ('Criaturas míticas'),
    ('Fantasmas'),
    ('Historias de tesoros ocultos');

-- Insertar Provincias
INSERT INTO provincias (id, name)
VALUES (1, 'San José'),
    (2, 'Alajuela'),
    (3, 'Cartago'),
    (4, 'Heredia'),
    (5, 'Guanacaste'),
    (6, 'Puntarenas'),
    (7, 'Limón');

-- Insertar Cantones
INSERT INTO cantones (id, name, province_id)
VALUES (1, 'San José', 1),
    (2, 'Escazú', 1),
    (3, 'Desamparados', 1),
    (4, 'Alajuela', 2),
    (5, 'San Ramón', 2),
    (6, 'Cartago', 3),
    (7, 'Paraíso', 3),
    (8, 'Heredia', 4),
    (9, 'Liberia', 5),
    (10, 'Puntarenas', 6),
    (11, 'Limón', 7);

-- Insertar Distritos
INSERT INTO distritos (id, name, canton_id)
VALUES (1, 'Carmen', 1),
    (2, 'Escazú Centro', 2),
    (3, 'San Rafael Abajo', 3),
    (4, 'Alajuela Centro', 4),
    (5, 'San Ramón Centro', 5),
    (6, 'Oriental', 6),
    (7, 'Paraíso Centro', 7),
    (8, 'Heredia Centro', 8),
    (9, 'Liberia Centro', 9),
    (10, 'Puntarenas Centro', 10),
    (11, 'Limón Centro', 11);

-- Insertar 10 Leyendas de Costa Rica
INSERT INTO leyendas (
        title,
        description,
        category_id,
        date,
        district_id,
        created_at,
        updated_at
    )
VALUES (
        'La Llorona',
        'El alma en pena de una madre que llora a su hijo perdido.',
        4,
        '1900-01-01',
        1,
        NOW(),
        NOW()
    ),
    (
        'El Cadejos',
        'Un perro fantasma que protege a los borrachos y castiga a los malvados.',
        3,
        '1850-01-01',
        2,
        NOW(),
        NOW()
    ),
    (
        'El Segua',
        'Un espíritu que se aparece a los hombres infieles con una cara de caballo.',
        3,
        '1800-01-01',
        3,
        NOW(),
        NOW()
    ),
    (
        'La Carreta sin Bueyes',
        'Una carreta espectral que anuncia la muerte.',
        4,
        '1890-01-01',
        4,
        NOW(),
        NOW()
    ),
    (
        'El Tesoro de la Isla del Coco',
        'Un tesoro escondido por piratas en la Isla del Coco.',
        5,
        '1700-01-01',
        5,
        NOW(),
        NOW()
    ),
    (
        'El Diablo en la Catedral',
        'Se dice que el Diablo ayudó a construir la Catedral de Cartago.',
        1,
        '1600-01-01',
        6,
        NOW(),
        NOW()
    ),
    (
        'La Tulevieja',
        'Un espíritu de una mujer que perdió a su hijo y ahora asusta a los viajeros.',
        3,
        '1900-01-01',
        7,
        NOW(),
        NOW()
    ),
    (
        'La Casa Embrujada de Heredia',
        'Una casa en Heredia donde ocurren fenómenos paranormales.',
        4,
        '2000-01-01',
        8,
        NOW(),
        NOW()
    ),
    (
        'El Fantasma del Hospital San Juan de Dios',
        'Apariciones de monjas y pacientes en este hospital.',
        4,
        '1950-01-01',
        9,
        NOW(),
        NOW()
    ),
    (
        'El Padre sin Cabeza',
        'Un sacerdote sin cabeza que aparece en las noches de luna llena.',
        4,
        '1900-01-01',
        10,
        NOW(),
        NOW()
    );