with open('yo.txt') as f:
    content=f.read() 

content= content.replace("donkey","@#$$%^^^")

with open('yo.txt','w') as f:
    f.write(content)



