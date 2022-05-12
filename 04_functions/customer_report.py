"""
Builds a Customer report for
sales order
"""

def print_customer_address(name, city, state, street):
    """prints a composed address"""
    customer_address = f"{name}\n{street}\n{city}, {state}"
    print(customer_address)


def calculate_order_total(qty, cost):
    """Multiplies qty by cost to calculate total"""
    return qty * cost


def print_customer_report():
    """Prints a customer report"""
    print("Shipping address:")
    print_customer_address(
        "Some Name",
        "San Diego",
        "CA",
        "123 Main st.",
    )
    print("Order Total:")
    order_total = calculate_order_total(10, 2.99)
    #rounded = round(order_total, 2)
    #print(rounded)
    print(order_total)

print_customer_report()