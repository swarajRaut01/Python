#creating a file with srings
f=open('D:/swaraj/myfile.txt','w')
print('enter text (@ at end):')
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")
f.close()
