#Vinh Pham
# 12/6/16
# Lab 14 - Construct classes: Fruit, Apple, and Orange, and create a main() in form of a store.



class Fruit(object):                        #Fruit Class
    def __init__(self, description= "", cost=0.00, calories=0):
        self.set_description(description)
        self.set_cost(cost)
        self.set_calories(calories)

    def __str__(self):                      #Returns the attributes in orderly manner
        return "Item description: {}; Cost: {:.2f}; Calories: {}"\
               .format(self.description,self.cost,self.calories)
    def __rep__(self):
         return self.__str__()

    def set_description(self,description):  #Setters for attributes
        self.description = description
    def set_cost(self, cost):
        self.cost = cost
    def set_calories(self,calories):
        self.calories = calories
        
    def get_description(self):              #Getters for attributes
        return self.description
    def get_cost(self):
        return self.cost
    def get_calories(self):
        return self.calories

    def __gt__(self,other):                 #Over-riding methods for personal use relevant to cost
        return self.cost > other.cost
    def __gte__(self,other):
        return self.cost >= other.cost
    def __lt__(self,other):
        return self.cost < other.cost
    def __lte__(self,other):
        return self.cost <= other.cost
    def __eq__(self,other):
        return self.cost == other.cost
    def __ne__(self,other):
        return self.cost != other.cost

    def eat(self):                          #It no longer exists
        self.set_description("(eaten)")
        self.set_cost(0.00)
        self.set_calories(0)


class Apple(Fruit):                         #Apple class
    def __init__(self,description="",cost=0.00,calories=0):
        Fruit.__init__(self,description,cost,calories)  #Uses __init__ from Fruit class
        self.core = False

    def core(self):
        if not self.core:
            self.set_description(self.description+"(cored)")
            self.set_cost(self.cost-((.20)*self.cost))
            self.set_calories(self.cost-((.20)*self.cost))
            self.core = True

class Orange(Fruit):
    def __init__(self,description="",cost=0.00,calories=0,peeled=False):    #One more parameter
        Fruit.__init__(self,description,cost,calories)
        self.peeled = peeled

    def peel(self):
        self.peeled = True

    def eat(self):                          #Over-riding eat(self) from Fruit class
        if self.peeled:
            Fruit.eat(self)
        else:
            raise(AttributeError)           #You can't eat an unpeeled orange

    def __str__(self):                      #Over-riding __str__(self) so we can show 'peeled'
        return "Item description: {}; Cost: {}; Calories: {}; Peeled: {}"\
               .format(self.description,self.cost,self.calories,self.peeled)



def main(): #Also known as our test.
    print ("-----MANAGER MODE-----")
    choice = input("Do you want to create an Apple or Orange? Type 'quit' to quit: ")
    fruit_list = []

    while choice.lower() != "quit":
        while choice.lower() not in ["apple","orange","quit"]:
            choice = input("Choice not valid. Please enter 'Apple', 'Orange', or 'quit': ")
        
        if choice.lower() == "apple":
            fruit_list.append(Apple("store front", 1.50, 100))
        elif choice.lower() == "orange":
            fruit_list.append(Orange("store front",1.75,110))
        choice = input("Do you want to create an Apple or Orange? Type 'quit' to quit: ")


    print ("-----SALE MODE-----")
    while len(fruit_list) != 0:
        print ("Here is the list of fruits: ")
        for item in fruit_list:             #Possible selections
            print ("{} for ${:.2f}".format(item.description,item.cost))
        
        bill = 0    #Initialize the bill
        choice2 = input("Do you want to add an apple or orange to your bill? Type 'stop' to finish.: ")
        item_list = []  #Initialize the final checkout list
        while choice2 != "stop":
            if choice2.lower() == "apple":
                if Apple("store front", 1.50, 100) not in fruit_list:
                    print ("Item not in list. Please try again.")   #Prevents error
                    pass
                else:
                    bill += 1.50
                    fruit_list.remove(Apple("store front", 1.50, 100))
                    item_list.append(Apple("store front", 1.50, 100))
            elif choice2.lower() == "orange":
                if Orange("store front", 1.75, 110) not in fruit_list:
                    print ("Item not in list. Please try again.")
                    pass
                else:
                    bill += 1.75
                    fruit_list.remove(Orange("store front",1.75,110))
                    item_list.append(Orange("store front",1.75,110))
            
            print ("")
            print ("Here is the list of fruits")
            for item in fruit_list:
                print ("{} for ${:.2f}".format(item.description,item.cost))
                
            if len(fruit_list) == 0:    #Can't sell if there's nothing else to buy.
                    print ("No more fruit in fruit_list")
                    break
            else:
                choice2 = input("Do you want to add an apple or orange to your bill? Type 'stop' to finish.: ")

        
        print ("\n-----Checkout-----")
        for item in item_list:
            print(item)

        bill += .065*bill   #For tax
        bill += .15*bill    #Our customers are VERY generous.
        
        print ("Total:${:.2f}".format(bill))    #Formality

        if len(fruit_list) != 0:
            print ("\n-----NEXT CUSTOMER PLEASE!-----") #We still have fruit!

     print ("WE'RE OUT OF FRUITS FOR TODAY. COME BACK TOMORROW!")       

    

    


              

def test():
    my_fruit = Fruit("red",4.50,50)
    print (my_fruit)
    your_fruit = Fruit("blue",2.00,20)
    print (my_fruit > your_fruit)
    my_orange = Orange("or",1.50,20,True)
    

    
        
        
