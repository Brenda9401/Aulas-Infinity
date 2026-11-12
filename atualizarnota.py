import sqlite3

def criar_tabela():
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Alunos (
            id INTEGER PRIMARY KEY,
            nome Text,
            idade INT,
            cidade TEXT
        )
    ''')
    cur.close()
    conn.close()

def inserir_alunos(lista_de_alunos):
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()

    cur.executemany('INSERT INTO Alunos VALUES (?, ?, ?, ?)', lista_de_alunos)
    conn.commit()
    cur.close()
    conn.close()


def listar_alunos():
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM Alunos')
    alunos = cur.fetchall()
  
    cur.close()
    conn.close()    
    return alunos

def atualizar_nome(id, novo_nome):
    conn = sqlite3.connect('escola.db')
    cur = conn.cursor()

    comando_update = 'UPDATE Alunos SET nome = ? WHERE id = ?'
    cur.execute(comando_update, (novo_nome, id))
    
    conn.commit()
    cur.close()
    conn.close()

lista_de_alunos = [
    (1, 'Ricardo', 24, 'Contagem'),
    (2, 'Brenda', 26, 'Belo Horizonte'),
    (3, 'Bianca', 17, 'Sabará'),
    (4, 'Gabriel', 28, 'Belo Horizonte')
]

criar_tabela()
# inserir_alunos(lista_de_alunos)
atualizar_nome(2, 'Brenda Hellen')