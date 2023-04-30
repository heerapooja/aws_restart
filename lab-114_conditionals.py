#Working with Conditionals

#Exercise 1: Working with the if statement
ip = input("Do you need ti ship a package? (Enter yes or no): ")
if ip =="yes":
    print("We can help you ship that package")
#Exercise 2: Working with the else statement
else:
    print("Please come back when you need to ship a package. Thank you.")

#Exercise 3: Working with the elif statement
ip =  input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if ip=="stamps":
    print("We have many stamp designs to choose from.")
elif ip=="envelop":
    print("We have many envelope sizes to choose from.")
elif ip=="copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    