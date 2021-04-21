class Store: 
    def __init__(self, name):
        self.name = name
        self.product = []
    
    #methods

    def add_product(self, new_product):
        self.product.append(new_product)
        return self
    
    def sell_product(self, id):
        for i in self.product:
            id = i
            print("Item #{}:").format(id)
        return self
    

class Product: 
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    #methods

    def update_price(self, percent_change, is_increased): 
        if is_increased == True:
            self.price += percent_change
        else:
            self.price -= percent_change
        return self
    
    def print_info(self):
        print("Name: {}, Category: {}, Price: ${}").format(self.name, self.category, self.price)
        return self

    
    #creation

    vons = Store("Vons")
    costco = Store("Costco")
    wholefoods = Store("Whole Foods")

    vons.add_product("Watermelon").add_product("Mango").add_product("Papaya").add_product("Strawberries")
    costco.add_product("Muffins").add_product("Pizza").add_product("Chicken Bake").add_product("Trail Mix")
    wholefoods.add_product("Alternative Chips").add_product("Coconut Yogurt").add_product("Sushi Veggie Roll").add_product("Silk Almond Milks")

    #remove a product
    vons.sell_product(0)

    print(vons.product)
    print(costco.product)
    print(wholefoods.product)

    print(vons.product)






