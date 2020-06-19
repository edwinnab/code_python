#a list is mutable, ordered, enclosed using square brackets
#example
my_fruits = ["mango", "apples","pineapples","oranges"]
my_numbers = [1,2,3,4,5,6,6,7]
#display the list
print(my_fruits[1])
#call individual items in a list using index
print(my_numbers[0])
#iterate over items
for i in my_fruits:
    print(i)
    #we can also access items using negative index starting with -1
print(my_fruits[-1])
#concatinate string items of a list using +
print("I love eating " + my_fruits[3])
#modify items in a list using index
my_fruits[1]="oranges"
print(my_fruits)
#slicing in list
print(my_fruits[0:1])
#to display the begin of the list we omit the inclucive integer
print(my_fruits[:3])
#end of the list we omit the exclusive
print(my_fruits[0:])
#negative integers can also be used
print(my_fruits[-4:])
my_integers = [1,2,3,45, 56,67,78,89,90,9,0,34,76,23,56,78,7,45,66,334]
#strides meaning how many items to move after the first has been retrieved
#python default stride is 1
print(my_integers[2:10:2])
#use + and - to concatinate lists
print(my_integers + my_fruits)
#use the * operator to multiply lists
print(my_fruits * 2)
print(my_integers * 2)
#to populate and automate lists we use the compound operators += and *=
for fruits in range(1, 4):
    my_fruits += ["Bananas"]
    print(my_fruits)
    #to remove items from a list use the keyword del
del(my_fruits[3])
del(my_integers[1:7])
print(my_fruits)
print(my_integers)
#to access items within nested lists we use indices
nested_list = [[1,2,3,5,6,7], ["sharon", "mwangi", "kigen", "ryan", "sensba"]]
print(nested_list[1][1])
print(nested_list[0][1])