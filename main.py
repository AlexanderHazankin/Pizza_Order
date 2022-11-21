print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you want? S, M, or L. ")
while size != "S" and size != "M" and size != "L":
    size = input("Please, enter one of three options: S, M or  L. ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":   # This can be changed by else statement
    bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N. ")
while add_pepperoni != "Y" and add_pepperoni != "N":
    add_pepperoni = input("Please, enter Y or N. ")
if add_pepperoni == "Y" and size == "S":
    bill += 2
elif add_pepperoni == "Y" and size == "M" or size == "L":   # This can be changed by else statement
    bill += 3

extra_cheese = input("Do you want extra cheese? Y or N. ")
while extra_cheese != "Y" and extra_cheese != "N":
    extra_cheese = input("Please, enter Y or N. ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
