restaurant ="Welcome to restaurant. Here's the Menu:"
print(restaurant)
menu ={
    "pizza":40,
    "pasta":50,
    "burger":60,
    "coffee":80
}
print(menu)
order1 = input("enter your first order:").lower()
total = menu.get(order1)
print("order of",order1,"has been added")
choice=input("Do you want to order anything else? (yes/no):").lower()
if choice=="yes":
    order2=input("Enter item you want to order:").lower()
    total += menu.get(order2, 0)
    print("order of",order2,"has been added")
else:
    print("Ok")
print("Total price to pay is:", total)
print("Thank You")
