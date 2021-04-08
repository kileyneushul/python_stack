#1. TASK: print "Hello World"
print("Hello World")

#2. print "Hello Kiley!" with the name in a variable
name = "Kiley"
print("Hello",name,"!") #with a ,
print("Hello " + name + "!") #with a +

#3.print "Hello 8!" with the number in a variable
name = 8
print("Hello", name, "!") #in order to eliminate space between name and "!" you will have to use an f string, % or concantenate
#print("Hello" + name + "!") #with a + we get an error (cannot interpolate variable and string)
print("Hello " +str(name) + "!") #convert the name variable into a string

#4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")

#5. Bonus print "I love to eat bread and eggs." with the % placeholder formatting
fave_food1 = "I love to eat %s" % "bread"
fave_food2= "and %s." % "eggs"

print(fave_food1, fave_food2)



