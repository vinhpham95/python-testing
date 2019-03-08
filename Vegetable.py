# Vinh Pham
# 11/22/16
# Lab 12
# Create a class of Vegetable with 3 items, and create a digital market.

class Vegetable(object): # Vegetables
    """Class of Vegetables"""
    def __init__(self, new_PC='', new_name='', new_description='', new_PPU = 0):
        self.PC = new_PC
        self.name = new_name
        self.description = new_description
        self.PPU = new_PPU
    def __str__(self):
        # print "In __str__ method"
        return "{} ({}) is {} for ${} per unit".\
            format(self.name, self.PC, self.description, self.PPU)
    
    def get_PC(self):               # To return attribute values
        return self.PC
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_PPU(self):
        return self.PPU
    
    def set_PC(self, new_PC):       # To set attribute values
        self.PC = new_PC
    def set_name(self,new_name):
        self.name = new_name
    def set_description(self, new_description):
        self.color = new_description
    def set_PPU(self, new_PPU):
        self.PPU = new_PPU



def main(): # Digital Market
    lettuce_head = Vegetable("A1","Lettuce Head","it doesn't talk",.75)  # Assign items to class
    bean = Vegetable("B1","Bean","magical of course",1.50)
    spinach = Vegetable("S1","Spinach","great for eyes",2.25)

    print("Welcome to my Vinh's Veggie Cart")
    print("Today, we have for sale:")
    print(" 1. {} - {}".format(lettuce_head.get_name(),lettuce_head.get_description()))
    print(" 2. {} - {}".format(bean.get_name(),bean.get_description()))
    print(" 3. {} - {}".format(spinach.get_name(),spinach.get_description()))
    print(" 4. Done, check out")
    item_purchase = int(input("What would you like to purchase? "))
    
    total_lettuce_head_count = 0 # Keeping tally for receipt
    total_bean_count = 0
    total_spinach_count = 0
    total_cost = 0
    
    while item_purchase != 4: # Type 4 to check-out
        if item_purchase == 1:
            lettuce_head_count = int(input("{} are ${:.2f} per unit. How many? ".\
                                       format(lettuce_head.get_name(),lettuce_head.get_PPU())))
            total_lettuce_head_count += lettuce_head_count
            total_cost += lettuce_head_count*lettuce_head.get_PPU()
            
        if item_purchase == 2:
            bean_count = int(input("{} are ${:.2f} per unit. How many? ".\
                                       format(bean.get_name(),bean.get_PPU())))
            total_bean_count += bean_count
            total_cost += bean_count*lettuce_head.get_PPU()
            
        if item_purchase == 3:
            spinach_count = int(input("{} are ${:.2f} per unit. How many? ".\
                                       format(spinach.get_name(),spinach.get_PPU())))
            total_spinach_count+= spinach_count
            total_cost += spinach_count*spinach.get_PPU()

        print("Today, we have for sale:")
        print(" 1. {} - {}".format(lettuce_head.get_name(),lettuce_head.get_description()))
        print(" 2. {} - {}".format(bean.get_name(),bean.get_description()))
        print(" 3. {} - {}".format(spinach.get_name(),spinach.get_description()))
        print(" 4. Done, check out")
        item_purchase = int(input("What would you like to purchase? "))
        
        print ("Your total cost is ${:.2f}".format(total_cost))

    print("Here's your final receipt:") # Check-out
    if total_lettuce_head_count > 0:
        print(" {} Lettuce Heads".format(total_lettuce_head_count))
    if total_bean_count > 0:
        print(" {} Bean".format(total_bean_count))
    if total_spinach_count > 0:
        print(" {} Spinach".format(total_spinach_count))
    print("Your total cost is ${:.2f}.".format(total_cost))
    print("Thank you, come again!.")
    
        
    

def test(): # To test (obviously)
    my_veg = Vegetables("A15","Banana","A banana",.25)
    print( my_veg.get_PC() ) #Prints A15
    print( my_veg.get_PPU() ) #Prints .25
    print (my_veg.get_name() )
    print (my_veg.get_description() )
    
    my_veg.set_PC("B15") #Changes my_veg's product code
    print( my_veg.__str__() ) #Prints something like "Banana (B15) is A banana for $.25 per unit"

def test2():
    lettuce_head = Vegetable("A1","Lettuce Head","it doesn't talk",.75)
    if lettuce_head.get_PC() !="A122":
        print ("wth")
