#exveptation information is program

try:
    print(10/0)

except ZeroDivisionError as  msg:
    print("the type a exceptation:",type(msg))
