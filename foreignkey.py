import sqlite3

def criar_tabelas_relacionadas():
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()

    #É obrigatório executar o comando abaixo para que as chaves estrangeiras funcionem
    cur.execute('PRAGMA foreign_keys = ON')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Categorias (
            ID INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL UNIQUE
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Materiais (
            ID INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            
            Categoria_ID INTEGER,
            FOREIGN KEY (Categoria_ID) REFERENCES Categorias(ID)
        )
    ''')

    conn.commit()
    cur.close()     
    conn.close()

def inserir_categorias(categorias):
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')

    cur.execute('INSERT INTO Categorias (titulo) VALUES (?)', ('SQL',))
    categoria_id = cur.lastrowid #Pega o ID da última categoria inserida

    titulo_material = 'Aula de Update de SQLite3'

    cur.execute('INSERT INTO Materiais (titulo, Categoria_ID) VALUES (?, ?)', (titulo_material, categoria_id))
    
    conn.commit()  
    conn.close()
    cur.close()

    criar_tabelas_relacionadas()
    inserir_categorias([Papelaria, Informática, Eletrônica, Matemática, Física, Química, Biologia, História, Geografia, Filosofia, Sociologia])

def juntar_tabelas():
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON')

    cur.execute('''
        SELECT Materiais.titulo, Categorias.titulo
        FROM Materiais 
        INNER JOIN Categorias ON Materiais.Categoria_ID = Categorias.ID
    ''')

    resultados = cur.fetchall()

    for titulo_material, titulo_categoria in resultados:
        print(f'Material: {titulo_material} | Categoria: {titulo_categoria}')

    conn.close()
    cur.close()