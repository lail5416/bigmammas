import sys #sys bruges til at kunne afslutte programmet rigtigt
from MenuKort import MenuKort 
from BigMammaHjemmeside import *


def testrun():
    Menu = MenuKort()
    Menu.MakeMenuKort()
    Menu.AddPizza("Meat Lovers Pizza",["Tomat", "Ost","skinke","pepperoni","kebab","cocktail-Pølser"], 80) #Tilføjer en ekstra pizza til listen
    Menu.ShowMenuKort()


    Menu.AddOrder([6], "Hans Olo", True)
    print(Menu.TakeOrderCatalog[0])

    Menu.AddOrder([3,6], "Flot fyr", True)

    for order in Menu.TakeOrderCatalog:
        print(order)
#vi tilføjer 1 ordrer fra Hans Olo og 1 ordre fra Flot fyr, som så bestiller 2 pizzaer

def run(): #Programmet er lavet til at det er en medarbejder der står og tager imod ordre i løbet af en arbejdsdag
    Menu = MenuKort()
    Menu.AddPizza("Margherita",["Tomat", "Ost"], 69)
    Menu.AddPizza("Vesuvio",["Tomat", "Ost","skinke"], 75)
    Menu.AddPizza("Capricciosa",["Tomat", "Ost","skinke", "champignon"], 80)
    Menu.AddPizza("Calzone",["Tomat", "Ost","skinke", "champignon"], 80)
    Menu.AddPizza("Quattro Stagioni",["Tomat", "Ost","skinke", "champignon", "rejer", "peberfrugt"], 85)
    Menu.AddPizza("Marinara",["Tomat", "Ost","rejer", "muslinger", "hvidløg"], 85)
    Menu.AddPizza("Vegetarian",["Tomat", "Ost","grøntsager"], 80)
    Menu.AddPizza("Italiana",["Tomat", "Ost","løg", "kødsauce"], 75)
    Menu.AddPizza("Gorgonzola",["Tomat", "gorgonzola","løg", "champignon"], 75)
    Menu.AddPizza("Contadina",["Tomat", "Ost","Oliven", "champignon"], 75)
    Menu.AddPizza("Naples",["Tomat", "Ost","ansjoser", "oliven"], 79)
    Menu.AddPizza("Vichinga",["Tomat", "Ost","skinke", "champignon","peberfrugt","hvidløg", "chili (stærk)"], 80)
    Menu.AddPizza("Calzone Special",["Tomat", "Ost","skinke", "rejer", "kødsauce"], 80)
    Menu.AddPizza("Esotica",["Tomat", "Ost","skinke", "rejer", "annanas"], 80)
    Menu.AddPizza("Tonno",["Tomat", "Ost","Tun", "rejer"], 85)
    Menu.AddPizza("Sardegna",["Tomat", "Ost","cocktail pølser", "bacon", "løg", "æg"], 80)
    Menu.AddPizza("Romana",["Tomat", "Ost","skinke", "bacon", "løg"], 78)
    Menu.AddPizza("sole",["Tomat", "Ost","skinke", "bacon", "æg"], 78)
    Menu.AddPizza("Big Mamma",["Tomat", "Gorgonzola","rejer", "Asparges", "parma skinke"], 90)

    def tagOrdre():
        OrderList = [] #Starter med en tom liste
        print("- indtast nummer på den ønskede pizza og tryk enter")
        print("- afslut din ordre ved at trykke F = finish ")
        NyOrdre = ""
        while NyOrdre == "": #Spørger efter et pizzanummer så længe det er en tom string
            NyOrdre = input(">>>> ")
            if NyOrdre != "F":
                try: #Hvis brugeren ikke har trykket F, så kommer der try - except for at lave int om til str
                    NyOrdre = int(NyOrdre)
                    if NyOrdre > 0 and NyOrdre < len(Menu.PizzaCatalog)+1: #len = længe på pizzakatalog (hvilke numrer programmet godtager)
                        OrderList.append(NyOrdre)
                    else:
                        print("Den Ønskede Pizza findes ikke på menukortet")
                        NyOrdre = ""
                except ValueError:
                    print("That's not an int!")
                NyOrdre = ""
            elif NyOrdre == "F":
                break
        

# Går videre til at lave og printe kvittering
        print("- indtast venligst dit navn:")
        navn = input(">>>> ")
        print("- Ønsker du takeaway? \n tast y = yes eller n = no ")
        inputGood= False
        while inputGood == False:
            takeaway = input(">>>> ")
            if takeaway == "y":
                takeaway = True
                inputGood= True
            elif takeaway == "n":
                takeaway = False
                inputGood= True
            else:
                inputGood= False

        
        Menu.AddOrder(OrderList, navn, takeaway)
        ordreID = len(Menu.TakeOrderCatalog)
        print(Menu.TakeOrderCatalog[ordreID-1]) #Printer selve ordren, længden af OrderCatalog

        return True


# Et while loop der holder programmet kørende
    tempVar = False
    while tempVar == False:

        print( "\nVelkommen Til Big Mommas Pizza !!! \n")
        print("Q = Quit")
        print("Vil du se MenuKortet ? \n")
        BrugerSvar = input("y = yes eller n = no\n>>>> " ) #Muligheder for at quit, se menukort eller bare bestille med det samme
        
        tempSvar = False
        while tempSvar == False: #et while loop indtil brugeren giver et brugbart svar
            if BrugerSvar == "y":
                Menu.ShowMenuKort()
                print("\nVi er Klar til at tage din ordre")
                tempSvar = tagOrdre()
            elif BrugerSvar == "n":
                print("\nVi er Klar til at tage din ordre")
                tempSvar = tagOrdre()
            elif BrugerSvar == "Q":
                print("Tak For Besøget\n")
                tempSvar = True
                for order in Menu.TakeOrderCatalog:
                    print(order)
                sys.exit()
            else:
                print("\nDet Forstår vi ikke")
                BrugerSvar = input("y = yes eller n = no\n>>>> ")
                tempSvar = False





# program starten

choice = input("\nønsker du \n 1: test run \n 2: run \n 3: hjemmeside \n>> ")
if choice == str(1):
    testrun()
elif choice == str(2):
    run()
elif choice == str(3):
   app.run()
else:
    sys.exit()