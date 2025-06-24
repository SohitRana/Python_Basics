# a function is a block of code that performance a specific task. Function help in organizing code, reusing code, and improving readability.


## syntax
# def function_name(parameters):
#     """docstring"""
#     # function boby
#     return expression



#num = int(input("enter the number"))
# if num%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")



# with function

# def even_or_odd(num):
#     """this function finds even or odd"""
#     if num%2==0:
#         print("the number is even")
#     else:
#         print("the number is odd")

# ## call this function
# even_or_odd(21)

##function with multiple parameters
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# def add(a,b):
#     return a+b
# result = add(num1,num2)
# print("The sum is:", result)

##default parameters

def greet(name="guest"):
    print(f"hello{name} welcome to code")
greet("krish")