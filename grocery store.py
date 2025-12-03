# Grocery store items with prices
grocery_items = {
    'apple': 50,
    'banana': 30,
    'milk': 120,
    'bread': 60,
    'eggs': 150,
    'rice': 200,
    'oil': 250
}

cart = {}

# Show all items
def show_items():
    print("\nAvailable Grocery Items:")
    for item, price in grocery_items.items():
        print(f"- {item.title()} : Rs {price}")
    print()

# Add item to cart
def add_to_cart():
    item = input("Enter item name to add: ").lower()
    if item in grocery_items:
        qty = int(input(f"Enter quantity of {item}: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"{qty} {item}(s) added to cart.")
    else:
        print("Item not found.")

# View cart
def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for item, qty in cart.items():
        price = grocery_items[item]
        subtotal = price * qty
        total += subtotal
        print(f"- {item.title()} x {qty} = Rs {subtotal}")
    print(f"Total: Rs {total}\n")

# Checkout
def checkout():
    if not cart:
        print("Cart is empty. Nothing to checkout.")
    else:
        view_cart()
        print("Thank you for shopping with us!")
    exit()

# Main menu loop
while True:
    print("\n--- Grocery Store Menu ---")
    print("1. View Items")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_items()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
