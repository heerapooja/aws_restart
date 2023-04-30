#Working with Lists, Tuples, and Dictionaries

#Exercise 1: Introducing the list data type
fruits= ["apple", "banana", "cherry"] #creation
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
fruits[2]="orange"
print(fruits)

#Exercise 2: Introducing the tuple data type
# Defining a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Exercise 3: Introducing the dictionary data type
#Defining a dictionary
fruits_dictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(fruits_dictionary)
print(type(fruits_dictionary))

#Accessing a dictionary by name
print(fruits_dictionary["Akua"])
print(fruits_dictionary["Saanvi"])
print(fruits_dictionary["Paulo"])
