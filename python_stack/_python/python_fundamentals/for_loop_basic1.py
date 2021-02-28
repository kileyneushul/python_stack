#1. Basic - Print all intergers from 0 to 150
for x in range(0,151,1):
    print(x)

def basic():
    for x in range(151):
        print(i)
basic()

#2. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for x in range(0,1001,1):
    if x % 5 == 0 and x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print (x)

def multiples_of_five():
    for x in range (5,1001,5):
        print x
multiples_of_five()

#3. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

total = 0
for x in range (0, 500000):
    if x % 2 == 1:
        total += x
print(total)

def woah_huge():
    final_sum=0
    for x in range(1,500000,2):
        final_sum += 1
    print(final_sum)
woah_huge()

#4. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for x in range (2018, 0, -4):
        print (x)

def countdown_by_fours():
    for i in range (2018, 0, -4):
        pring(i)
countdown_by_fours()

#5. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for x in range (lowNum,highNum+1):
    if x % mult == 0:
        print(x)

def flexible_counter(low_num, high_num, mult):
  for i in range(low_num, high_num + 1):
    if i % mult == 0:
      print(i)

flexible_counter(2, 9, 3)




    



    
    
