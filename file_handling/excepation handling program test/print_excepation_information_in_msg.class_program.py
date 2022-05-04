#print excepation information as a msg in program

try:
    print(10/0)

except ZeroDivisionError as msg:
   print("the type of error:",msg.__class__)
