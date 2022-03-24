
def str_to_numb(n):
    if n == 'zero':
        n = 0
    elif n == 'one':
        n = 1
    elif n == 'two':
        n = 2
    elif n == 'three':
        n = 3
    elif n == 'four':
        n = 4
    elif n == 'five':
        n = 5
    return n
    
#Create a function that will be in charge of knowing what type of operation will be done and will return the result of the operation
def calc(n1, operator, n2):
    n1 = int(str_to_numb(n1))
    n2 = int(str_to_numb(n2))
    if operator == "plus":
        return n1 + n2
    elif operator == "minus":
        return n1 - n2
    else:
        return "Not supported operation"
    
# Define a list with the numbers and one with the operations so that when the user tries to enter a 
##character that is not in those lists, it will continue asking him to enter the data until he meets the requirement

numbers = ["zero","one","two","three","four","five"]
operations = ["plus", "minus"]

n1 = input("Please type a number from zero to five: ")
while n1 not in numbers:
    n1 = input("Please type a number from zero to five: ")
    
operator = input("Please type sum or subtract as + or -: ")
while operator not in operations:
    operator = input("Please type sum or subtract as + or -: ")

n2 = input("Please type a number from zero to five: ")
while n2 not in numbers:
    n2 = input("Please type a number from zero to five: ")
    
print(calc(n1, operator, n2))