# When Python attempts to read a source file, the following happens:
# - The interpreter sets several special variables, such as __name__
# - The interpreter executes the code in the file.

from lunch_menu import LunchMenu

cafe_menu = LunchMenu()
cafe_menu.add_beverages("tea")
cafe_menu.add_beverages("coffee")
cafe_menu.add_food("bagel")
cafe_menu.generate()
