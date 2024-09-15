# Steps to Build:
# Create an empty list to represent the shopping cart.
# Use a loop to continuously ask the user for input.
# Display a menu with options to add, remove, view the cart, or exit.
# Use if-else statements to handle the user's choices.



def show_menu():
    print("select an option:")
    print("1, Add an itom:")
    print("2, Remove an element:")
    print("3, View cart :")
    print("4, Exit:")

cart = []
while True:
    show_menu()
    
    choise = input("Enter your input (1-4):")
     
    
    if choise == '1':
        items = input("Enter itom for add to cart:")
        cart.append(items)
        print(f"{items} added to cart")
      

# shopping_cart_list = []

# user_input = input("Enter your itoms:")

# for i in user_input:
#     shopping_cart_list.append(i)
# print(shopping_cart_list)







