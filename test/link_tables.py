import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def link_tables():
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()