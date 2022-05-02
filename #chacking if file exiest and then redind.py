#chacking if file exiest and then redind data import os,sys


fname=input('enter filename')

if os.path.isfile(fname):
    f=open(fname,'r')

    else:
        print(fname+'does ont exist')
        sys.exit()

print('the file content are:')
str=f.read()
print(str)
f.close()