f=open('sample.txt','r')
t = f.read()
if 'hello' in t :
    print("yes")
else:
    print("no!")
    
f.close()