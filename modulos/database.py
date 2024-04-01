import sqlite3

class Database:
    def __init__(self):
        self.conexao = sqlite3.connect('database/financasPessoais.db')
        
    
    