#1 Countdown


def countdown(num):
    nums_list = []
    for val in range(num,-1,-1):
        nums_list.append(val)
    return nums_list

print(countdown(12))
print(countdown(5))

#2 Print and Return

def two_num_list(nums_list):
    print(nums_list[0])
    return(nums_list[1])

print(two_num_list([4500, 6090358]))

#3 First Plus Length

def first_plus_length(numberList):
    return numberList[0]+ len(numberList)
print(first_plus_length([5,4,3,5,6,7]))


#4 Values Greater than Second

def values_greater_than_second(listOnes):
    listNew = []
    #second value original list
    second_val = listOnes[1]
    #scan through the original list, find values greater than second value and add them to the new list
    for val in range(len(listOnes)):
        if listOnes[val] > second_val:
            listNew.append(listOnes[val])
    print(len(listNew))
    return listNew
    if len(listOnes) < 3:
        return False
print(values_greater_than_second([1,8,9,5,4,10,7,12,4,-9]))

#5 This Length, That Value

def this_length_that_value(size, value):
    list_int = []
    for num_times in range(size):
        list_int.append(value)
    return list_int

print(this_length_that_value(30, 6))
    

    





