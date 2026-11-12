#Update => Atualizar

import sqlite3

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

lista_de_alunos = [
    (1, 'Ricardo', 24, 'Contagem'),
    (2, 'Brenda', 26, 'Belo Horizonte'),
    (3, 'Bianca', 17, 'Sabará'),
    (4, 'Gabriel', 28, 'Belo Horizonte')
]

cur.executemany('INSERT INTO Alunos VALUES (?, ?, ?, ?)', lista_de_alunos)

nome = 'Brenda Sales'
id = 2

cur.execute('''
    UPDATE Alunos
    SET nome = ?
    WHERE id = ?
''', (nome, id))

conn.commit()

cur.execute('SELECT * FROM Alunos')

Alunos = cur.fetchall()

for id, nome, idade, cidade in Alunos:
    print(f'ID:{id} | Nome:{nome} | Idade:{idade} | Cidade:{cidade}')