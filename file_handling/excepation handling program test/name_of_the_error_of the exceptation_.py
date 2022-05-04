#print the class name of the error

try:
    print(10/0)

except ZeroDivisionError as msg:
    print("the type of exceptation:",msg.__class__.__name__)

