class LunchMenu:
    """Tracks items on the lunch menu"""

    def __init__(self):
        self.beverages = []
        self.food = []

    def add_food(self, food):
        """Adds food to the menu"""
        self.food.append(food)

    def add_beverages(self, beverages):
        """Adds beverages to the menu"""
        self.beverages.append(beverages)

    def generate(self):
        print("Food:")
        for food in self.food:
            print("- " + food)

        print("Beverages:")
        for beverage in self.beverages:
            print("- " + beverage)

if __name__ == "__main__":
    # Creating an instance of LunchMenu
    my_menu = LunchMenu()

    # add food and beverages to the instance
    my_menu.add_food("soup")
    my_menu.add_food("sandwich")
    my_menu.add_food("salad")
    my_menu.add_beverages("coffee")
    my_menu.add_beverages("wine")
    my_menu.add_beverages("beer")

    # Print the menu
    my_menu.generate()

    veg_menu = LunchMenu()
    veg_menu.add_food("cabbage soup")
    veg_menu.add_food("black bean soup")
    veg_menu.add_food("corn chowder")


    meat_menu = LunchMenu()
    meat_menu.add_food("T-bone steak")
    meat_menu.add_food("tenderloin")
    meat_menu.add_food("chicken sandwich")

    print("Vegetarian Menu:")
    veg_menu.generate()

    print("Meat Menu:")
    meat_menu.generate()