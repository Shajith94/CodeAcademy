# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slives = prices.count(2)
print(num_two_dollar_slives)

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage",], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices) #2d list 

pizza_and_prices.sort() #stores the pizzas in the order of increasing price
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0][1] #shows the first element

priciest_pizza = pizza_and_prices[-1][-1] #shows the priciest pizza which in this case in the last element from the asc list

pizza_and_prices.pop() #removes anchovies since it is the last element of the  list

pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices) #used append to insert the new data and then used sort to have in fit in on price ascending

three_cheapest = pizza_and_prices[:3] #to store the 3 lowest cost pizza
print(three_cheapest)















