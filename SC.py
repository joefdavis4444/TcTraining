for _ in range(8):
    print('\n')

print("WELCOME TO SHOPPING CART BY JOE")
for _ in range(2):
    print('\n')
print("Here is what we have")
inventory = ['Apples', 5, 1.50,
             'Banana', 10, 2.5,
             'Orange', 8, 2.75,
             'Mango', 0, 8.00,
             'Grapes', 20, 3.75]
# print (*inventory, sep="\n")

print(f"{"Item":<15}{"Qty":<15}{"Cost Per":<15}")
# print inventory
if len(inventory) < 15:
    print("it dont fit")
else:
    for i in range(5):  # Loop for 5 rows
        start_index = i * 3
        # Extract 3 elements for the current row
        item1 = inventory[start_index]
        item2 = inventory[start_index + 1]
        item3 = inventory[start_index + 2]

        # Print the elements with formatting for alignment
        print(f"{item1:<15}{item2:<15}{item3:<15}")

shopping_list = []

# creating list for shopper
print("What would you like?")
item = " "
amount = 0

while item is not "done":

    item = input("Which item would you like or if done please say done: ")
    if item in inventory:
        if len(inventory) < 15:
            print("item not present")
        else:
            for j in range(5):  # Loop for 4 rows
                start_index = j * 3
                # Extract 3 elements for the current row
                item1 = inventory[start_index]
                item2 = inventory[start_index + 1]
                item3 = inventory[start_index + 2]

                if item1 == item:
                    amount = input("how many do you want: ")
                    if int(amount) > item2 or int(amount) < 0:
                        print("we do not have enough")
                    else:
                        shopping_list.append(item1)
                        shopping_list.append(float(amount))
                        shopping_list.append(float(amount) * item3)
                        print(int(amount) * item3)
                        inventory[start_index + 1] = (float(inventory[start_index + 1]) - float(amount))
                else:
                    print("Searching for item")

                    # Print the elements with formatting for alignment
                # print(f"{item1:<15}{item2:<15}{item3:<15}")


    else:
        print("item not present")
        if item == "done":
            break

# Take personal info
name = input("Please enter your name: ")

phone_number = input("Please enter your phone_number: ")

address = input("Please enter your address: ")

distance = input("Please enter your distance in miles from store: ")
distance_cost = float(distance) * 1.5

# print bill
if len(shopping_list) == 0:
    distance = 0

for _ in range(5):
    print('\n')

print("-----------------------------------Bill----------------------------------")
# print ("{:>5}{:>20}{:>20}{:>20}".format(name,phone_number,address, (int(distance)*1.5)) )


# print (shopping_list)

# print (type(rows))
print(f"{"item":<15}{"Qty":<15}{"Cost":<15}")
length = len(shopping_list)
rows = int(length / 3)
if len(shopping_list) < length:
    print("outie")
else:
    for c in range(rows):
        start_index = c * 3
        # Extract 3 elements for the current row
        item1 = shopping_list[start_index]
        item2 = shopping_list[start_index + 1]
        item3 = shopping_list[start_index + 2]

        # Print the elements with formatting for alignment
        print(f"{item1:<15}{item2:<15}{item3:<15}")

point = 2
cost = 0
while point < len(shopping_list):
    cost += float(shopping_list[point])
    point += 3

total_cost = cost + distance_cost
print("Name: " + name)
print("Phone Number: " + phone_number)
print("Address: " + address)
print("Delivery Charge: " + str(distance_cost))
if len(shopping_list) == 0:
    total_cost = 0

for _ in range(2):
    print('\n')
print("Delivery costs $1.50 per mile is added to Total")
print("Total Cost is: $" + str(total_cost))



