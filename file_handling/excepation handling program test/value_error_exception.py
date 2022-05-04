#value error exceptation hadling\

try:
    x=int(input('enter the first number'))
    y=int(input('enter the second number'))
    print('the resuit:',x/y)

except(ZeroDivisionError, ValueError)as msg:
    print('the raised excaption:',msg.__class__.__name__)
    print('description of excepation:',msg)
    print('plz provide valid inpute only....')
    
