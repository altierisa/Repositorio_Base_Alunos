import sqlite3

# Nome do arquivo do banco de dados
produto = 'produtos.db'

# Script para criar a tabela
script_produtos = '''
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL,
    estoque INTEGER NOT NULL
);
'''

# Criação da tabela
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(script_produtos)
        con.commit()
        print('Tabela criada com sucesso!')
except sqlite3.OperationalError as e:
    print('Erro na criação da tabela:', e)

# Inserção de um único produto
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute('''
            INSERT INTO Produtos (nome, preco, categoria, estoque)
            VALUES (?, ?, ?, ?)
        ''', ('Notebook Dell', 2500.00, 'Eletrônicos', 15))
        con.commit()
        print('Produto inserido com sucesso!')
except sqlite3.OperationalError as e:
    print('Erro ao inserir produto:', e)

# Inserção de múltiplos produtos
produtos = [
    ('Notebook', 3500.00, 'Eletrônicos', 10),
    ('Smartphone', 2200.00, 'Eletrônicos', 15),
    ('Geladeira', 4800.00, 'Eletrodomésticos', 5),
    ('Camiseta', 59.90, 'Vestuário', 50),
    ('Cafeteira', 320.00, 'Eletrodomésticos', 8)
]

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.executemany('''
            INSERT INTO Produtos (nome, preco, categoria, estoque)
            VALUES (?, ?, ?, ?)
        ''', produtos)
        con.commit()
        print('Produtos inseridos com sucesso!')
except sqlite3.OperationalError as e:
    print('Erro:', e)

# Consulta para listar os produtos
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Produtos')
        resultados = cur.fetchall()
        print('Conteúdo da tabela Produtos:')
        for linha in resultados:
            print(linha)
except sqlite3.OperationalError as e:
    print('Erro:', e)

sql = 'UPDATE Produtos SET preco = ? WHERE id =  ?'
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,(3500.00,1))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro:', e)

    res = cur.execute('SELECT nome FROM Produtos')
    res.fetchall()

    for linha in cur.execute('SELECT nome, preco FROM Produtos ORDER BY nome'):
        print(linha)

sql = 'DELETE FROM Produtos WHERE id =  ?'
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,(1,))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro:', e)

con.close()