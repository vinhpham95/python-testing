#Vinh Pham
#10/25/16
#Generate a readable list sorted by maker to display average city mpg and hwy mpg.


# highest mileage data
# from http://www.fueleconomy.gov/FEG/download.shtml

def create_mileage_list(epa_file):
    """Create a list of cars and mileage from epa_file."""
    # 2a create a mileage list and initialize it to empty
    mileage_list = []

    for line in epa_file:              # 2b. get each line from the file
        if line[0:5] == 'CLASS' or\
                 'VAN' in line or\
                 'PICKUP' in line:   
            continue                 # skip pickups, vans and the header line
        line_list = line.split(',')           # 2bI. csv => split on comma
        # create tuple: (mileage, make, model)
        car_tuple = (int(line_list[8]), int(line_list[9]), line_list[1], line_list[2])
        mileage_list.append(car_tuple)        # 2bII. append tuple
    return mileage_list

def average_city_hwy_by_maker(car_tuples):
    maker_list = []                             # Making a list of makers
    for car_tuple in car_tuples:
        if car_tuple[2] not in maker_list:
            maker_list.append(car_tuple[2])

    
    list_of_maker_lists = []                    # Making a list of lists, in format [Maker,0,0,0]
    objects_in_list_of_maker_list = []          # for each list(item) of the list.
    for maker in maker_list:
        objects_in_list_of_maker_list = []
        objects_in_list_of_maker_list.extend([maker,0,0,0])
        list_of_maker_lists.append(objects_in_list_of_maker_list)

    for maker_tuple in list_of_maker_lists:     # Updating the total city and hwy mpg of every maker
        for car_tuple in car_tuples:
            if maker_tuple[0] == car_tuple[2]:  
                maker_tuple[1]=maker_tuple[1]+car_tuple[0] 
                maker_tuple[2]=maker_tuple[2]+car_tuple[1]
                maker_tuple[3]=maker_tuple[3]+1 # This serves as counter so we can later find average

    for maker_tuple in list_of_maker_lists:             # Find the average of city/hwy mpg by maker
        maker_tuple[1]=maker_tuple[1]/maker_tuple[3]    # using counter
        maker_tuple[2]=maker_tuple[2]/maker_tuple[3]

    list_of_tuples = []
    for maker_tuple in list_of_maker_lists:         # Converts all the lists(items) in the list into tuples
        list_of_tuples.append(tuple(maker_tuple))   # by making a new list.
        
            
    return list_of_tuples   # The end result is a list of tuples in format
                            # (Maker, AVG City MPG, AVG HWY MPG, Counter)

    


##############################################
# 1. open EPA data file
epa_file = open("epaData.csv", "r")

print("EPA Car Mileage")
print() # blank line

# 2a create a mileage list
mileage_list = create_mileage_list(epa_file)
#print (mileage_list)

averages = average_city_hwy_by_maker(mileage_list) # Assign a call function, and format by printing
print ("{:<20s}{:>20s}{:>20s}".format("MAKER","CITY MPG AVERAGE","HWY MPG AVERAGE"))
for item in averages:
    print ("{:<20s}{:>20.2f}{:>20.2f}".format(item[0],item[1],item[2]))
    

# 3. find max and min mileage
#    mileage_list is a list of tuples (mileage, make, model)
#    max(mileage_list)[0] finds the max mileage tuple and extracts the mileage
##max_mileage = max(mileage_list)[0]
##min_mileage = min(mileage_list)[0]
##
##print("Max and Min Mileage: ", max_mileage, min_mileage)
##print()  # print blank line
##
###4. create a list of all cars with max and min mileage: list of car tuples
##max_mileage_list, min_mileage_list = \
##                find_max_min_mileage(mileage_list,max_mileage,min_mileage)
##
##print("Maximum Mileage Cars:")
##for car_tuple in max_mileage_list:
##    print("  ", car_tuple[1], car_tuple[2])
##print("Minimum Mileage Cars: ")
##for car_tuple in min_mileage_list:
##    print("  ", car_tuple[1], car_tuple[2])
##
