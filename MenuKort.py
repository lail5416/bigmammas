

from TakeOrder import TakeOrder
from Pizza import MYpizza
import random



class MenuKort(object):
    
    def __init__(self): #def __init__ kaldes en constructer - vi laver 2 tomme lister som attributter
        
        self.PizzaCatalog = []
        self.TakeOrderCatalog=[]


    def MakeRandomPizzas(self): #Bruges kun i testrun for at få et menukort for at arbejde med som test
        PizzaList = []
        ExtraToppings = ["Annanas", "Skinke", "Pepperoni", "Champignon", "Løg", "Dressing", "Salat", "Bacon", "kebab", "cocktail-pølser"]
        ToppingList = ["Tomat", "Ost"]
        for i in range(1,6):
            randInt = random.randint(0, len(ExtraToppings)-1)
            ToppingList.append(ExtraToppings[randInt])
            del ExtraToppings[randInt] #del = delete
            NewPizza = MYpizza(i, "Pizza" + str(i), ToppingList, 50)
            PizzaList.append(NewPizza)
            ToppingList = ["Tomat", "Ost"]
        return PizzaList
#for loop hvor der bliver tilføjet eller fjernet extratopping med random

    def MakeMenuKort(self):
        self.PizzaCatalog = self.MakeRandomPizzas()

    def AddPizza(self, name, topping, pris):
        ToppingList = topping
        newPizza = MYpizza(len(self.PizzaCatalog)+1, name, ToppingList ,pris )
        self.PizzaCatalog.append(newPizza)

    def AddOrder(self, pizzanumber, name, togo):
        PizzaList = []
        for number in pizzanumber:
            PizzaList.append(self.PizzaCatalog[number-1])
        order = TakeOrder(len(self.TakeOrderCatalog)+1, PizzaList, name, togo)
        self.TakeOrderCatalog.append(order)


    def ShowMenuKort(self):
        print("\n===================================================================================================\n")
        for pizza in self.PizzaCatalog:
            print(pizza)
        print("\n===================================================================================================\n")

    



