#functions are instructions packaged tigether
#use the keyword def to define functions
def hello_func():
    print("hello function!")
hello_func()

#functions allow us to re_use code 
#example instead of having to repeat code we just use functions
#this is called keeping our code DRY (Don't Repeat Yourself)


#pass shows that we will fill in code later


#hello_func()#to execute the function
#the paranthesis is a must to show that we are executing the function
#without the parathesis it is just equal to the function
def func_basics():
    return "function basics"
"""using the return keyword, makes our call function equal to the return value
when we run this it displays nothing
since we ain't doing anything with the string"""
func_basics()
"""using print""" 
print(func_basics())

#print(hello_func)#shows it is a function at a particular place in memory
#to execute

#print(hello_func())
#passing parameter
def parame_basic(morning):
    return "{} class!" .format(morning)
print(parame_basic("morning"))
#example two
#def person(gender, age):s
 #   return "I am {}, {} years old ".format(gender,age)
#print(person("Female", "18"))

#example three we can specify a default value
def person_one(age, gender = "male"):
    return"I am {}, of {} years old".format(gender, age)
print(person_one("19"))

#passing in positional argunments and keyword argunments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info("maths", "arts", "english", "science", "algebra", age = 23, name = "Limah", Class = "form one", gender = "female")
#example three
def comp_scienc(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ["calculus", "algebra", "programming", "system analysis", "networking"]
stude_inform = {"name" : "Harriet Ndoa", "age": 34, "course" : "computer science"}
comp_scienc(*courses, **stude_inform)