# Andrew Chavez
# Independent Project 2
# Personal Python project created for coursework
# This program allows the user to order items from a delivery service


print ("Welcome to Andrew's Cookie Delivery Service!")
print ("Let's put an order together for you. What would you like?")

purchases = []
choice = ""
totalCost = 0.000
while choice != "Q":
    if totalCost > 0:
        print ("Would you like something else?")
    # Menu items
    print ("C: Chocolate Chip Cookie   $1.50")
    print ("S: Sugar Cookie            $2.00")
    print ("M: Midnight Mint Cookie    $1.50")
    print ("D: Daily Special Cookie    $2.00")
    print ("O: Oatmeal Raisin Cookie   $3.75")
    choice = str(input ("Type the letter of your choice and then press enter. Press 'Q' when your order is complete. "))
    # Space
    print ("")
    # Adds Price to total cost and item to order list
    if choice == "C":
        totalCost = totalCost + 1.50
        purchases.append("Chocolate Chip Cookie")
    elif choice == "S":
        totalCost = totalCost + 2
        purchases.append("Sugar Cookie")
    elif choice == "M":
        totalCost = totalCost + 1.50
        purchases.append("Midnight Mint Cookie")
    elif choice == "D":
        totalCost = totalCost + 2
        purchases.append("Daily Special Cookie:")
    elif choice == "O":
        totalCost = totalCost + 3.75
        purchases.append("Oatmeal Raisin Cookie")
    
# Asks the user if they are a rewards member and gives a discount based on their answer
reply = input ("Are you a rewards member? Please enter 'Y' or 'N': ")
if reply == "Y":
    discountCost = float(totalCost - (totalCost*(0.10)))

# Prints the list of items ordered and their cost before and after savings
print ("Thank you for your order: " + str(purchases))
print ("The cost of your items is: $ " + str(totalCost))
if reply == "Y":
    print ("The cost after your savings is: $ " + str(round(discountCost,2)))
else:
    print ("The cost after your savings is: $ " + str(round(totalCost,2)))



