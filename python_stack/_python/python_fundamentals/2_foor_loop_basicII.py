#1 Biggie Size
def biggie_size(nums):

    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i] = "big"
    return nums 

print(biggie_size([1,-4,5,0,-4,-6,10]))

#2 Count Positives
def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

#3 Sum Total

def sum_total(listE):
    sum = 0
    for val in listE:
        sum = sum + val 
    return sum
print(sum_total([1,5,7,12,20,2]))
print(sum_total([9,8,7,6,5,4,3,2,1]))
print(sum_total([1,2,3]))

#4 Average

def average(average):
    sum=0
    for val in average:
        sum += val #here the total value of sum will increase by val every iteration
    return sum/len(average)
print(average([1,2,3,4,6]))  

#5 Length

def list_length(lengthList):
    count=0
    for number in lengthList: 
        count += 1 #difference between this and average is that the value will only increment by one as the for loop loops through
    return count
print(list_length([0,1,2,3,4]))

#6 Minimum

def minimum(minimum_num):
    if len(minimum_num) == 0:
        return False
    min = minimum_num[0]
    for val in minimum_num:
        if val < min: 
            min = val
    return min 
print(minimum([5,3,7,3,0]))
print(minimum([]))

#7 Maximum 

def maximum(maximum_num):
    if len(maximum_num) == 0:
        return False
    max = maximum_num[0]
    for val in maximum_num:
        if val > max: 
            max = val
    return max
print(maximum([5,3,7,3,0]))
print(maximum([]))

#8 Ultimate Analysis

def ultimate_analysis(lst):
    knlist = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return knlist
    else:
        knlist['sum_total']=0
        knlist['maximum']= lst[0]
        knlist['minimum']= lst[0]
    for val in lst:
        if val > knlist['maximum']:
            knlist['maximum'] = val
        elif val < knlist['minimum']:
            knlist['minimum'] = val

        knlist['sum_total'] += val
        knlist['length'] += 1

    knlist['average'] = knlist['sum_total']/len(lst)

    return knlist

print(ultimate_analysis([1,2,3,1,5,7]))
print(ultimate_analysis([]))

#9 Reverse List

def reverse_list(hello):
    half_len = int(len(hello)/2)
    for i in range(half_len):
        hello[i] , hello[len(hello) - 1 - i] = hello[len(hello)-1 - i], hello[i]
    return hello

print(reverse_list([5,6]))
print(reverse_list([37,2,1,-10,5]))
print(reverse_list([45,7,6,8,-3,0]))



    


    

