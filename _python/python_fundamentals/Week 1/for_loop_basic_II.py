#1 Biggie Size

def biggieSize(listNums):
    for val in range (listNums[0], len(listNums), 1):
        if listNums[val] >= 0:
            listNums[val] = "big"
    return listNums

print(biggieSize([0,-1,4,98,-5,-47,0,7,8,9,10,30,-4,34]))

#2 Count Positives

def countPositives(listNums):
    sumPosValues = 0
    for val in (listNums):
        if val > 0:
            sumPosValues += 1
    listNums[len(listNums)-1]= sumPosValues
    return listNums
print(countPositives([1,2,3,4,-9,-6,-5,4]))
print(countPositives([1,5,6,7]))

#3 Sum Total

def sumTotal(listNums):
    sumOfValues = 0
    
    for num in (listNums):
        sumOfValues += num
    return sumOfValues

print(sumTotal([0,3,4,5,6]))
print(sumTotal([0,1,2,1,2]))

#4 Average

def averageValues(listNums):
    sum = 0

    for num in listNums:
        sum += num
    
    return float(sum)/float(len(listNums))

print(averageValues([9,8,7,6,5,4,3,2,1]))
print(averageValues([1,2,3]))
print(averageValues([0,1,2]))
print(averageValues([15,12]))

#5 Length

def lengthOfList(listNums):
    sum = 0
    for num in listNums:
        sum += 1
    return sum
print(lengthOfList([0,1,2,3]))
print(lengthOfList([1,2,3]))
print(lengthOfList([1,2,3,4,5,6,7,8,9,0,1,2,3]))

#6 Minimum

def minimum(listy):
    if len(listy) == 0:
        return False
    min = listy[0]
    for why in listy:
        if why < min:
            min = why
    return min

print(minimum([0,1,2,3]))
print(minimum([6,7,2,1,9,0,1]))
print(minimum([0,0,0,0,-30,8,-2]))
print(minimum([]))

#7 Maximum

def maximum(list1):
    if len(list1) == 0:
        return False
    max = list1[0]
    for why in list1:
        if why > max:
            max = why
    return max

print(maximum([0,1,2,3]))
print(maximum([6,7,2,1,9,0,100]))
print(maximum([0,0,0,0,30,8,-2]))
print(maximum([]))

#8 Ultimate Analysis

def ultimate_analysis(dictList):

    knlist = {
        'sumTotal' : None,
        'Minimum' : None,
        'Maximum' : None,
        'Average' : None,
        'Length' : 0
    }

    if len(dictList) == 0:
        return knlist
    else:
        knlist['sumTotal'] = 0
        knlist['Minimum'] = dictList[0]
        knlist['Maximum'] = dictList[0]

    for i in dictList:
        if i < knlist['Minimum']:
            knlist['Minimum'] = i
        elif i > knlist['Maximum']:
            knlist['Maximum'] = i
        knlist['sumTotal'] += i
        knlist['Length'] += 1
    knlist['Average'] = knlist['sumTotal']/len(dictList)

    return knlist

print(ultimate_analysis([0,1,3,4,5,6,-9]))
print(ultimate_analysis([4,2,1,7,89,90]))
print(ultimate_analysis([-5,-1,0,4,3,2]))

#9

def reverseList(listNums):
    half_len = int(len(listNums)/2)
    for num in range(half_len):
        listNums[num] , listNums[len(listNums) - 1 - num] = listNums[len(listNums) - 1 - num], listNums[num]
    return listNums

print(reverseList([8,9,9,0,9,1,2]))
print(reverseList([45,45,21,21]))
 




