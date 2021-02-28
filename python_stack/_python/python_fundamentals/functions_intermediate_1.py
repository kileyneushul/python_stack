import random
def randInt(min= 0 , max= 100):
    range = max-min
    return (random.random()*range + min)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=101, max=500))