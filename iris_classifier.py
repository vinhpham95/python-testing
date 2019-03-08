# Vinh Pham
# 11/15/16
# Lab 11 - Analyze a Iris string data, classify each item, and measure inaccuracy.

# 1. sepal length in cm
# 2. sepal width in cm 
# 3. petal length in cm 
# 4. petal width in cm 
# 5. class: -- Iris Setosa, Iris Versicolour, Iris Virginica

import math

def make_data_set(file_name):  # file_name is a string
    '''Read file file_name (str); return list of tuples in format:
       id, diagnosis, 9 attributes.'''
    input_set_list = []

# open file. Fix the error checking
    input_file = open(file_name)

    for line_str in input_file:
        line_str = line_str.strip()  # strip off end-of-line character " \n"
        # if a '?' in the patient data, skip that patient
        if '?' in line_str:
            continue
        a1,a2,a3,a4,id_str= line_str.split(',')
        if id_str == 'Iris-setosa': # diagnosis is "Iris-setosa"
            id_str = 's'
        elif id_str == 'Iris-versicolor':
            id_str = 've'  # diagnosis is "Iris-versicolor"
        elif id_str == 'Iris-virginica':
            id_str = 'vi' # diagnosis is "Iris-virginica"
            
        patient_tuple=id_str,float(a1),float(a2),float(a3),float(a4),
        input_set_list.append(patient_tuple)
    return input_set_list


def sum_lists(list1,list2):
    """Element-by-element sums of two lists of 4 items."""
    sums_list = []
    for index in range(len(list1)):
        sums_list.append(list1[index]+list2[index])
    return sums_list

def make_averages(sums_list,total_int):
    """Convert each list element into an average by dividing by the total."""
    averages_list = []
    for value_int in sums_list:
        averages_list.append(value_int/total_int)
    return averages_list


def train_classifier(training_set_list):
    """Build a classifier using the training set."""
    Iris_setosa_sums_list=[0]*4    # list of sums Iris-setosa of  attributes
    Iris_setosa_count=0            # count of Iris-setosa patients
    Iris_virginica_sums_list=[0]*4 # list of sums of Iris-virginica attributes
    Iris_virginica_count=0         # count of Iris-virginica patients
    Iris_versicolor_sums_list=[0]*4 # list of sums of Iris-versicolor attributes
    Iris_versicolor_count=0         # count of Iris-versicolor patients
    

    for patient_tuple in training_set_list:
        if patient_tuple[0]=='s':   # if Iris-setosa diagnosis
            # add Iris-setosa attributes to Iris-setosa total
            Iris_setosa_sums_list=sum_lists(Iris_setosa_sums_list,patient_tuple[1:])
            Iris_setosa_count += 1
        elif patient_tuple[0]=='vi':   # if Iris-virginica diagnosis
            # add benign attributes to benign total
            Iris_virginica_sums_list=sum_lists(Iris_virginica_sums_list,patient_tuple[1:])
            Iris_virginica_count += 1
        elif patient_tuple[0]=='ve':   # if Iris-versicolor diagnosis
            # add Iris-versicolor attributes to malignant total
            Iris_versicolor_sums_list=sum_lists(Iris_versicolor_sums_list,patient_tuple[1:])
            Iris_versicolor_count += 1

    # find averages of each set of benign or malignant attributes
    Iris_setosa_averages_list=make_averages(Iris_setosa_sums_list,Iris_setosa_count)
    Iris_virginica_averages_list=make_averages(Iris_virginica_sums_list,Iris_virginica_count)
    Iris_versicolor_averages_list=make_averages(Iris_versicolor_sums_list,Iris_versicolor_count)

    # separator values for each attribute averages benign and malignant
    classifier_list=[Iris_setosa_averages_list,Iris_virginica_averages_list,Iris_versicolor_averages_list]

    print (classifier_list)
    return classifier_list

def classify_test_set(test_set_list, classifier_list):
    '''Given test set and classifier, classisfy each patient in test set;
       return list of result tuples: (id,benign_count,malignant_count,diagnosis)'''
    result_list = []
    # for each patient
    for patient_tuple in test_set_list:
        # print (patient_tuple)
        id_str = patient_tuple[0]
        result = [id_str]
        s_distance =distance(patient_tuple[1:],classifier_list[0])
        vi_distance =distance(patient_tuple[1:],classifier_list[1])
        ve_distance =distance(patient_tuple[1:],classifier_list[2])
        if s_distance < vi_distance and s_distance < ve_distance:
            result.append("s")
        elif (vi_distance < s_distance) and (vi_distance < ve_distance):
            result.append("vi")
        elif ve_distance < s_distance and ve_distance < vi_distance:
            result.append("ve")
                
        result_list.append(result)
        #print (result)
    return result_list

def distance(list1,list2):
    """Calculates distance of 4-dimensional list"""
    distance = float(math.sqrt((list1[0]-list2[0])**2+(list1[1]-list2[1])**2+(list1[2]-list2[2])**2+(list1[3]-list2[3])**2))
    return distance

def report_results(result_list,test_set_list):
    '''Check results and report count of inaccurate classifications.'''
    total_count=0
    inaccurate_count = 0
    for result in result_list:

        if result[0] != result[-1]:
            inaccurate_count += 1
        total_count += 1
    print("Of ",total_count," patients, there were ",\
          inaccurate_count," inaccuracies")

def main():

    print("Reading in training data...")
    training_file = "training.data.txt"
    training_set_list = make_data_set(training_file)
    print("Done reading training data.\n")

    print("Training classifier...")    
    classifier_list = train_classifier(training_set_list)
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_file = "test.data.txt"
    test_set_list = make_data_set(test_file)
    print("Done reading test data.\n")

    print("Classifying records...")
    result_list = classify_test_set(test_set_list, classifier_list)
    print("Done classifying.\n")

    report_results(result_list,test_set_list)

    print("Program finished.")
            

    
        
                
    

