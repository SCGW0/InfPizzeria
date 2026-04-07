# Vul hier de naam van je programma in:
# MCMpizzaria
#
# Vul hier jullie namen in:
# Maaren
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------
def maakTabellenAan():
    # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_pizzas(
    gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
    gerechtNaam TEXT NOT NULL,
    gerechtPrijs REAL NOT NULL);""")
    print("Tabel 'tbl_pizzas' a")

def printTabel(tabel_naam):
 cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
 opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
 print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegev

### --------- Hoofdprogramma  ---------------
maakTabellenAan()
printTabel('tbl_pizzas')
