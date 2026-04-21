import sqlite3
import random
import uuid

def GuidGen():
    return str(uuid.uuid4())

def ConnDB():
    return sqlite3.connect('loja.db')

def GenUser(index):
    return f'Usuario{index}'

def GenProduct(index):
    return f'Produto{index}'

def inserirdados(cursor):

    for i in range(1, 31):
        nome = GenUser(i)
        email = f'{nome.lower()}@example.com'
        senha = f'senha{i}'
        cursor.execute('''
        INSERT INTO usuarios (id, nome, email, senha)
        VALUES (?, ?, ?, ?)''', (GuidGen(), nome, email, senha))

    for j in range(1, 41):
        nome = GenProduct(j)
        descricao = f'Descricao do {nome}'
        preco = round(random.uniform(10.0, 1000.0), 2)
        quantidade = random.randint(1, 50)
        cursor.execute('''
        INSERT INTO produtos (id, nome, descricao, preco, quantidade)
        VALUES (?, ?, ?, ?, ?)''', (GuidGen(), nome, descricao, preco, quantidade))

def CreateDataBase(conn):

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')



    # somente na primeira execução é importante comentar as linhas 63, 64, 65 e descomentar a linha 67

    if cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="usuarios"').fetchone() is None and cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="produtos"').fetchone() is None :
      if cursor.execute('SELECT COUNT(*) FROM usuarios').fetchone()[0] == 0 and cursor.execute('SELECT COUNT(*) FROM produtos').fetchone()[0] == 0:
        inserirdados(cursor)
    
    # inserirdados(cursor)

    

    conn.commit()

def main():
    conn = ConnDB()

    CreateDataBase(conn)

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM usuarios')
    print(cursor.fetchall())


    conn.close()

if __name__ == "__main__":
    main()