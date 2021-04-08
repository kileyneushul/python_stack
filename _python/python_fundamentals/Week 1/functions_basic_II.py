#1 Countdown
def countdown(num):
    countdown_list = [] 
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list
print(countdown(40))
print(countdown(3))
print(countdown(85))

#2 Print and Return
def printAndReturn(two_num_list):
    print(two_num_list[0])
    return(two_num_list[1])
print(printAndReturn([1,2]))
print(printAndReturn([3,7]))
print(printAndReturn([45,67]))

#3 First Plus Length

def first_plus_length(num_list):
    return num_list[0] + len(num_list)
print(first_plus_length([9,2,3,4,5,6,7,8,9]))
print(first_plus_length([0,1,2,3]))
print(first_plus_length([100,102,103,104,6]))

#4 Vaues Greater than Second

def values_greater_than_second(num_list):
    #new list creation
    new_list = []

    #second value variable
    second_value = num_list[1]

    if len(num_list) < 3:
        return False

    for val in range(len(num_list)):
        if num_list[val] > second_value:
            new_list.append(num_list[val])
    print(len(new_list))
    return new_list

print(values_greater_than_second([1,2,3,4,5,6,7]))
print(values_greater_than_second([90,32,12,87,34,2]))
print(values_greater_than_second([6,9]))
print(values_greater_than_second([0,1]))

#5 This Length That Value

def sizeAndValue(size, value):
    createList = []
    for numberOfTimes in range (size): 
        createList.append(value)
    return(createList)

print(sizeAndValue(10,3))
print(sizeAndValue(90,5))
print(sizeAndValue(1,4))
print(sizeAndValue(1,3))







        
