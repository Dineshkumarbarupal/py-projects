manu = {
    "bargar": 50,
    "pizza": 150,
    "coffee": 80,
    "sandwich": 50
}
print("welcome to our restuarant...")
print(f"bargar = 50rs\npizza = 150rs\ncoffee = 80rs\nsandwich = 50rs\nFor cunfirm order = cunfirm")



def cafe_system():
    while True:
        item = input("Enter your food wich you want to order:")
        

        if item in manu:
            print(f"your ordered item {item} added succesfully.")     
        elif item == "ok":
            order_total = 0
            for price in item:
              order_total += price
            print("thank you for order.") 
            print(f"your total price is ")   
            break   
        elif item not in manu:
            print(f"Item {item} not in manu.")    

cafe_system()




