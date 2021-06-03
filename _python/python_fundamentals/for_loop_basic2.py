# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
a_list = []
def biggie_size(a_list):
    new_list = []
    for x in range(len(a_list)):
        if a_list[x] < 1:
            new_list.append(a_list[x])
        if a_list[x] > 0:
            new_list.append("big")
    print(new_list)
    return new_list
biggie_size([-1, 3, 5, -5])
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
a_list = []
def count_positives(a_list):
        new_list = []
        for int in range(len(a_list)):
            if a_list[int] > 0:
                new_list.append(a_list[int])
        long =  len(new_list)
        a_list[len(a_list)-1] = long
        return a_list
count_positives([1,6,-4,-2,-7,-2])
# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
a_list = []
def sum_total(a_list):
    sum(a_list)
    return sum(a_list)
sum_total([1,2,3,4])
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
a_list = []
def average(a_list):
    for int in range(len(a_list)):
        average1 = sum(a_list)/len(a_list)
    return average1
average([1,2,3,4])
# Length - Create a function that takes a list and 
# returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
a_list = []
def length(a_list):
    len(a_list)
    return len(a_list)
length([37,2,1,-9])
# Minimum - Create a function that takes a list of 
# numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
a_list = []
def minimum(a_list):
    if len(a_list) == 0:
        return "False"
    min = a_list[0]
    for int in range(len(a_list)):
        if a_list[int] < min:
            min = a_list[int]
    return min
minimum([])
# Maximum - Create a function that takes a list and 
# returns the maximum value in the array. If the list
# is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
a_list = []
def maximum(a_list):
    if len(a_list) == 0:
        return "False"
    max = a_list[0]
    for int in range(len(a_list)):
        if a_list[int] > max:
            max = a_list[int]
    return max
maximum([37,2,1,-9])
# Ultimate Analysis - Create a function that takes 
# a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of 
# the list.
# Example: ultimate_analysis([37,2,1,-9]) should 
# return {'sumTotal': 31, 'average': 7.75, 'minimum': 
# -9, 'maximum': 37, 'length': 4 }
a_list = []
dict = {
    'sumTotal': 0,    
    'average': 0,
    'minimum': 0,
    'maximum': 0,
    'length': 0
    }
def ultimate_analysis(a_list):
    sum(a_list)
    dict['sumTotal'] = sum(a_list)
    dict['average'] = sum(a_list)/len(a_list)
    min = a_list[0]
    for int in range(len(a_list)):
        if a_list[int] < min:
            min = a_list[int]
    dict['minimum'] = min
    max = a_list[0]
    for int in range(len(a_list)):
        if a_list[int] > max:
            max = a_list[int]
    dict['maximum'] = max
    dict['length'] = len(a_list)
    return dict
ultimate_analysis([37,2,1,-9])
# Reverse List - Create a function that takes a list 
# and return that list with values reversed. Do this 
# without creating a second list. (This challenge is 
# known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return 
# [-9,1,2,37]
a_list = []
def reverse_list(a_list):
    temp = a_list[0]
    a_list[0] = a_list[len(a_list)-1]
    a_list[len(a_list)-1] = temp
    temp2 = a_list[1]
    a_list[1] = a_list[len(a_list)-2]
    a_list[len(a_list)-2] = temp2
    return a_list
reverse_list([37,2,1,-9])