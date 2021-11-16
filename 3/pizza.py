import re


class Pizza:
    ingredients = {1: "Ham", 2: "Sausage", 3: "Bacon", 4: "Beef", 5: "Meatball", 6: "Spinach", 7: "Olive",
                   8: "Mushroom", 9: "Tomato", 10: "Eggplant", 11: "Garlic", 12: "Cheese", 13: "Pineapple", 14: "Onion", 15: "Caper"}
    flavors = {"Hawaiian": [1, 13], "Garden Feast": [6, 7, 8, 9, 10], "Meat Festival": [
        2, 3, 4, 5], "Carbonara": [3, 12], "Custom": []}

    def __init__(self, flavor: str, custom_ingreds: list):
        self.flavor = flavor
        self.ingredients = custom_ingreds if flavor == "Custom" else Pizza.flavors[
            flavor]

    def __str__(self):
        ingreds = []
        for i in self.ingredients:
            ingreds.append(Pizza.ingredients[i])

        return re.sub(r"'", '', f'{self.flavor} {tuple(ingreds)}')


class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order = PizzaOrder.total_orders
        self.pizza_list = []

        print(f"Pizza order {self.order}:")
        while 1:
            order = PizzaOrder.select_menu()
            self.pizza_list.append(Pizza(order[0], order[1]))
            quit = re.sub(r' ', '', input(
                'Do you want more pizzas (y/n)? ').lower())
            if quit == 'n':
                print(f"Pizza order {self.order}'s summary:")
                break

    def __str__(self):
        result = ''
        for i in range(len(self.pizza_list)):
            result += f"{i+1}. {self.pizza_list[i].__str__()}\n"
        return result

    @ staticmethod
    def select_menu():
        flavors = list(Pizza.flavors)
        ingreds = []
        for i in range(len(flavors)):
            print(f'{i+1}. {flavors[i]}')
        flavor = int(input('Select a flavor: '))
        if flavor == 5:
            print(re.sub(r"[{}']", '', str(Pizza.ingredients)))
            ingreds = [
                *map(int, input("Select id's of ingredients: ").split(" "))]
        return flavors[flavor-1], ingreds


if __name__ == '__main__':
    PizzaOrder.total_orders = 0
    for i in range(3):  # placing 3 pizza orders
        po = PizzaOrder()
        print(po)
