import psycopg2
import pandas as pd
import numpy as num
from PullTable import pull_table_in_postgresql, pull_record_in_postgresql, add_record_in_postgresql, \
    truncate_table_in_postgresql, edit_record_in_postgresql

print ("WELCOME TO SHOPPING CART BY JOE")
for _ in range(2):
    print('\n')
print ("Here is what we have")

#create a dictionary for the store and the shopping cart
joe_columns = ['items', 'quantity', 'cost']

joe_store = dict.fromkeys(joe_columns)
dataj = pd.DataFrame( pull_table_in_postgresql('joestore'),columns=['items', 'quantity', 'cost'])
print(dataj)
numarr = dataj.to_numpy()
#print(numarr)
#joe_store = pd.concat([joe_store, pull_table_in_postgresql('joestore')], ignore_index=True)
#cart = dict.fromkeys(joe_columns)
cart = pd.DataFrame()

#print(cart)

#pull_table_in_postgresql("joestore")
#done = "done"
response = " "
count = 0
itemcost = 0
while response is not "done":
    response = input("Which item would you like or if done please say done: ")
    if response == "done":
        print("response is done")
        break
    else:
        #print (response)
        #pull_record_in_postgresql(response)
        #if num.where(numarr == response):
        #if num.char.find(numarr, response) :
        f = num.where(numarr == response)[0]
        if f.size > 0:
           # print(num.where(numarr == response)[0])
            #print(numarr[num.where(numarr == response)[0]])
            #print(numarr[num.where(numarr == response)[0],1])
            count =input("How many of the items would you like?: ")
            c = int(numarr[num.where(numarr == response)[0], 1])
            cc = float(numarr[num.where(numarr == response)[0], 2])
            #print(c)
            if int(count) <= c :
                itemcost = cc * int(count)
                entry = pd.DataFrame({'items': [response], 'quantity': [count], 'cost': [itemcost]})
                #print(entry)
                cart = pd.concat([cart, entry], ignore_index=True)
                if (int(c)-int(count)) >=0:
                    edit_record_in_postgresql(response,int(c)-int(count) )

            if (int(c)-int(count)) < 0:
                print('OUTSIDE OF OUR QUANTITY ')
                #create a subtract def
            #parse row of item to get quantity and cost
                add_record_in_postgresql(response, count, itemcost)

        else:
            print('WE DO NOT HAVE THAT ITEM')



#Take personal info
nname = input("Please enter your name: ")


nphone_number = input("Please enter your phone_number: ")

naddress = input("Please enter your address: ")

ndistance = input("Please enter your distance in miles from store: ")
ndistance_cost= float(ndistance) * 1.5

print ("-----------------------------------Bill----------------------------------")
print(f"{"item":<15}{"Qty":<15}{"Cost":<15}")
#pull_table_in_postgresql("shoppingcart")
print(cart)
total = ndistance_cost + cart['cost'].sum()
print ("Name: " + nname)
print ("Phone Number: " + nphone_number)
print ("Address: " + naddress)
print ("Delivery Charge: " + str(ndistance_cost))
print("Delivery costs $1.50 per mile is added to Total")
print ("Total Cost is: $" + str(total))
truncate_table_in_postgresql()