#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x [1][0] = 15
print(x)
#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
print(students)
#3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)
#4. Change the value 20 in z to 30 
z[0]['y']=30
print(z)

#2.

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterateDictionary(some_list):
    for dictionary in some_list:
        string_type = ''
        for key, value in dictionary.items():
            string_type += f'{key} - {value}, '
        print(string_type)

iterateDictionary(students)

#3.
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
    
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4. 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for list_num in some_dict.keys():
        print(f"{len(some_dict[list_num])} {list_num.upper()}")
        for item in some_dict[list_num]:
            print(item)
        print('\n')

printInfo(dojo)
