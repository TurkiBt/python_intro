#Update Values in Dictionaries and Lists
x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

#Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(x):
    for k in x:
        for key, value in k.items():
            print(key, value)
        print('\n')

iterateDictionary(students)

print("===============================================")

#Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
print("\n")
iterateDictionary2('last_name', students)

print("===============================================")

#Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(x):
    for main, names in x.items():
        print(len(names), main)
        for name in names:
            print(name)
        print("\n")
printInfo(dojo)