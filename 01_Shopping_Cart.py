# Add items to the cart.
# View the items in the cart.
# Remove items from the cart.
# Exit the program.


# Steps to Build:
# Create an empty list to represent the shopping cart.
# Use a loop to continuously ask the user for input.
# Display a menu with options to add, remove, view the cart, or exit.
# Use if-else statements to handle the user's choices.


def show_cart():
    print("select an option")
    print("1, Add an itom in cart: ")
    print("2, Remove an itom:")
    print("3, Veiw cart:")
    print("4, Exit:")
  
cart = []

while True:
    show_cart()

    choise = input("Enter your choise:")

    if choise == "1":
        item = input("Enter the itom to add:")
        cart.append(item)
        print(f"{item} Add to cart:")
    

    elif choise == "2":
        item = input("Which item you want to remove:")
        if item in cart:
            cart.remove(item)
            print(f"Succesfully remove {item}")
        else:
            print(f"{item} not found in cart")

    elif choise == "3":
        if choise == 0:
            print("your cart is empty.")
        else:
            print("All items in cart")
            for i,item in enumerate(cart ,1):
                print(f"{i} , {item}")

    elif  choise == "4":
        print("Exit from cart")
        break
    else:
        print("an in valied item")
           

    


        










