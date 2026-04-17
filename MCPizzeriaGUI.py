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
def zoekKlant():
 #haal de ingevoerde_klantnaam op uit het invoerveld
 # en gebruik dit om met SQL de klant in database te vinden
 gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
 print(gevonden_klanten) # om te testen

 invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
 invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
 for rij in gevonden_klanten: #voor elke rij dat de query oplevert
    #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
    invoerveldKlantNr.insert(END, rij[0])
    #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
    invoerveldKlantnaam.insert(END, rij[1]) 

def zoekPizza():
 gevonden_Pizzas = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizzanaam.get())
 print(gevonden_Pizzas)

def toonMenuInListbox():
    listboxMenu.delete(0, END) #maak de listbox leeg
    listboxMenu.insert(0, "ID Gerecht Prijs")
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

def haalGeselecteerdeRijOp(event):
 #bepaal op welke regel er geklikt is
 geselecteerdeRegelInLijst = listboxMenu.curselection()[0]
 #haal tekst uit die regel
 geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)
 #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
 invoerveldGeselecteerdePizza.delete(0, END)
 #zet tekst in veld
 invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst) 

def voegToeAanWinkelWagen():
 klantNr = invoerveldKlantNr.get()
 gerechtID = invoerveldGeselecteerdePizza.get()
 aantal = aantalGekozen.get()
 MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
 winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
 listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
 for regel in winkelwagen_tabel:
    listboxWinkelwagen.insert(END, regel)

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

knopSluit = Button(venster, text="Afsluiten", width=10, height=1, command=venster.destroy)
knopSluit.grid(row=0, column=0)

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=1, sticky="W")

labelKlant = Label(venster, text="Klantnaam:")
labelKlant.grid(row=1, column=0, sticky="W")

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

labelKlantnr = Label(venster, text="Klantnummer:")
labelKlantnr.grid(row=2, column=0, sticky="W")

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

KnopZoekOpKlantNaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
KnopZoekOpKlantNaam.grid(row=1, column=3)

labelpizzanaam = Label(venster, text="Pizzanaam:")
labelpizzanaam.grid(row=3, column=0, sticky="W")

labelmogelijkheden = Label(venster, text="Mogelijkheden:")
labelmogelijkheden.grid(row=4, column=0, sticky="W")

invoerveldPizzanaam = Entry(venster)
invoerveldPizzanaam.grid(row=3, column=1, sticky="W")

listboxMenu = Listbox(venster, height=6, width=30)
listboxMenu.grid(row=4, column=1)
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=3, column=1, rowspan=10, sticky="E")
listboxMenu.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxMenu.yview)


ingevoerde_pizzanaam = StringVar()
knopZoekPizzaOpNaam = Button(venster, text="zoek pizza", command=zoekPizza)
knopZoekPizzaOpNaam.grid(row=3, column=3)

knopToonPizzas = Button(venster, text="Toon alle pizza's", command=toonMenuInListbox)
knopToonPizzas.grid(row=4, column=3)

labelGekozenpizza = Label(venster, text="Gekozen pizza:")
labelGekozenpizza.grid(row=5, column=0, sticky="W")

invoerveldGeselecteerdePizza = Entry(venster)
invoerveldGeselecteerdePizza.grid(row=5, column=1, sticky="W")

labelAantal = Label(venster, text="Aantal:")
labelAantal.grid(row=6, column=0)

aantalGekozen = StringVar()
AantalKnop = OptionMenu(venster, aantalGekozen, 1,2,3)
AantalKnop.grid(row=6, column=1)

knopVoegToe = Button(venster, text= "Voeg toe", command=voegToeAanWinkelWagen)
knopVoegToe.grid(row=6, column=2)

labelBestelling = Label(venster, text="Bestelling:")
labelBestelling.grid(row=7, column=0)

listboxWinkelwagen = Listbox(venster, height=4, width=30)
listboxWinkelwagen.grid(row=7, column=1)

#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
