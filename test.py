# This is a simple calculator
# Display this after evaluation

#create function for all operations
def Add(x, y):
    result = x + y
    return result
def sqrt(x):
    result = x*x
    return result
   
x = int(input('enter your x value: '))
y = int(input('enter your y value: '))
 
print(sqrt(y))
print(Add(x, y))
