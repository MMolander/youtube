# Classes provide a way to combine data with behavior
# Classes allow us to create nre types to work with
# we can instantiate new instances of classes


class MessagePrinter:
    name = ""

    def __init__(self, name):
        self.name = name

    def print_hello(self):
        print("Hello " + self.name)

    def print_hello_custom(self, custom_name):
        print("Hello " + custom_name)


printer_1 = MessagePrinter("Molle")
printer_2 = MessagePrinter("Foo")


printer_1.print_hello()
printer_2.print_hello()
printer_2.print_hello_custom("Baz")