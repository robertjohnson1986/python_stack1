#1 - First Challenge
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"] = "Bryant"

# In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
 }
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30

#2 - Second Challenge
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def iterateDictionary(some_list):
    for idx in students:
        for key in idx:
            print(key, "-", idx[key])
iterateDictionary(students)

#3 - Third Challenge
