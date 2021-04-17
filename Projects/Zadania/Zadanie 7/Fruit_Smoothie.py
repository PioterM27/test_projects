'''
Create a class Smoothie and do the following:

Create an instance attribute called ingredients.
Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
Ingredient	Price
Strawberries	$1.50
Banana	$0.50
Mango	$2.50
Blueberries	$1.00
Raspberries	$1.00
Apple	$1.75
Pineapple	$3.50

'''


ingredient_list = {'Stawberries': 1.50, 'Banana': 0.5, 'Mango': 2.50, 'Blueberries': 1.00,
                   'Rasberries': 1.75, 'Apple': 1.75, 'Pineapple': 3.50}


class Smoothie:
    def __init__(self, ing_list):
        self.ingredients = ing_list
        self.cost=0

    def get_cost(self):
        smoothie_value = 0
        for ingredient in self.ingredients:
            if ingredient in ingredient_list.keys():
                smoothie_value += ingredient_list[ingredient]

        # self.cost = smoothie_value
        self.cost=smoothie_value
        return smoothie_value
    def get_price(self):
        return self.cost*1.5

    def get_name(self):
        pass

s1 = Smoothie(["Banana", "Apple"])
s1.get_cost()
print(s1.cost)
print(s1.get_price())