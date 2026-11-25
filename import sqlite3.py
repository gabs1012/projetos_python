import sqlite3

conexao = sqlite3.connect('abrigo_cae.db')
cursor = conexao.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS Cae(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL UNIQUE,
  idade INTEGER,
  Status_saude TEXT
 )
''')

# Adicione esta linha LOGO APÓS criar a tabela e ANTES do INSERT
cursor.execute("DELETE FROM Cae") 


cursor.execute ("INSERT OR IGNORE INTO Cae (nome, idade, Status_saude) VALUES ('Thor', 4, 'Saudavél')")
conexao.commit()

cursor.execute("SELECT *FROM Cae")
caes_cadastrados = cursor.fetchall()

print("--- CÃES CADASTRADOS VIA PYTHON ---")
for cao in caes_cadastrados:
    print(f"ID: {cao[0]} | NOME: {cao[1]} | IDADE: {cao[2]} | SAUDE: {cao[3]} ")

conexao.close()