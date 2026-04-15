# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
# MCMpizzaria
#
# Vul hier jullie namen in:
# Maaren
# 
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

knopSluit = Button(venster, text="Afsluiten", width=10, height=1, command=venster.destroy)
knopSluit.grid(row=0, column=0)

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=17, column=4, sticky="W")



#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
