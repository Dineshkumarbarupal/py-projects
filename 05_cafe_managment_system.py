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
        item = input("Enter your food which you want to order:")
        
        
        
        if item in manu:
            price = manu[item]
            print(f"your ordered item {item} added succesfully.")     
        elif item == "ok":
            
            print("thank you for order.") 
            print(f"your total price is {price} ")   
            break   
        elif item not in manu:
            print(f"Item {item} not in manu.")    

cafe_system()




