"""
#integers
print(34)
#assign to a variable
num = 34
print(num)
#perform mathematical operations
#addition
num = 34
num2 = 45
#sum is a keyword to perform addition uses the operator +
sum = (num + num2)
print(sum)
#subtraction
print(num - num2)
#multiplication
print(num * num2)
#division integer division
print(num/num2)
#floor division
print(num//num2)
#check what data type yoy have by using the function type()
print(type(sum))
"""
"""
#float has decicimal points
num = 45.32
print(num)
#check type
print(type(num))
#float is not equal to an integer
"""
"""
#Boolean named after George Boole a mathematician
#used for logical operations
#True,False are special values in python thus start with a capital letter.
num = True
print(num)
#check type
print(type(num))
"""
"""
#strings is a sequence of one or more characters (letters, numbers ,symbols)
#sting can be either constant or variable
#store a string on a variable
my_str = "Edwinna"
print(my_str)
print(type(my_str))
#operations on strings 
#lists are mutable,use square brackets on list,
#access elements using indeces
my_list = ["money", "food", "clothes", "pencils"]
print(type(my_list))
#tuple use round brackets and are immutable
my_tuple = (1,2,3,4,5,6)
print(type(my_tuple))
#dictionaries use curly braces and have a key_value pair
my_dict = {"two": 2, "three": 3, "four": 4}
print(type(my_dict))
#sets non repetitive, curly braces
my_set = {"money", "love","family"}
print(type(my_set))
"""
#working with strings
#exist within double quotes ad single quotes
#whichever you choose to use just be consistent
#display using the print function
units = " this is a very long string "
print(type(units))
#manipulation of strings
#concatination +
#to have a space between the strings you use whitespaces inside the string
cs = "string"
print( cs + units)
print("Edwinna" + "  Bikeri")
#string replication, repeats the string several times uses the* operator
print("CODE UNTIL YOU CODE " *4)
#string literal (what we see in the source code including the quotation marks),
#string value is what we see after running the program,
#string literal
name = "Edwinna Bikeri"
#string value
print(name)
#quotes embed double quotes within single quotes
print('edwinna says, "hello"')
#apostrophe use the possessive apostrophe with double quotes
print("Edwinna's car")
#to display multiple lines use triple single/double quotes
print("this is my car")
#or triple multiple lines
print("""call it family,
        how amazing to have that,
        amazing i tell you
        am just tryin to show
        the use of triple quotes
        to display multiple lines""")
#use backslash \ for quotations
print("Edwinna says \"hello\"")
print("edwinna\'s car")
print("1.   maize" "2. love"    "3. beans")
print("sammy\'s says \"the baloon is red?\"")
#raw string tells python to ignore all the escape characters.
print(r"sammy's says this is the color red?")
print(r"sammy\'s says \"the baloon is red?\"")
print(name.upper())
print(name.lower())
print(len(name))
print(name.replace("Bikeri","Omwando"))
"""
"""
#boolean methods return True, False
#.isnumeric prints True if numeric
phone_number = "098279747"
print(phone_number.isnumeric())
#.isupper() accepts uppercase
name = "a ahsjakak3826282"
print(name.isupper())
#.isalpha accepts alphabets
school = "hakkVDSJYE"
print(school.isalpha())
#.isalnum accepts  alphanumerc
pasd ="njkj2889913931"
print(pasd.isalnum())
#.islower accepts lowercase
phone = "hjo b aeihwqwu"
print(phone.islower())
sent = "this is a sentenses to check something I've learnt"
mak = "this too so just follow"
print(reversed(mak))
print(mak.count("o"))