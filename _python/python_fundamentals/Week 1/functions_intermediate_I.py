import random
def randInt(min=0, max=100):
    range = max-min
    return (random.random()*range + min)
    
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=100))
print(randInt(min=74, max=75))







    