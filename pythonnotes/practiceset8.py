# def greatest(num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         print("THE GREATEST NUMBER IS:",num1)
#     elif(num2>num1 and num2> num3):
#         print("THE GREATEST NUMBER IS:",num2)
#     elif(num3>num1 and num3>num2):
#         print("THE GREATEST NUMBER IS:",num3)
#     else:
#         print("invalid input")


# num1=int(input("Enter number1:"))
# num2=int(input("Enter number2:"))
# num3=int(input("Enter number3:"))
# greatest(num1,num2,num3)





# def convert (cels):
#     fahr = cels* (9.0/5.0) + 32.0
#     print("The temperature after converting cel to fahr is:",fahr)
#     return fahr


# cels=float(input("Enter the celcuis:"))
# convert(cels)




#n=1+2+3+4+5...n-1 +n
# def natural(n):
#     if(n==1):
#         return 1
#     elif(n==0):
#         return 0
#     else:
#         sum= n+ natural(n-1)
#         return(sum)


# n=int(input("enter a number:"))
# print("the sum of natural numbers are: ", natural(n))





# print("hello ", end="")
# print("how ", end="")
# print("are ", end="")
# print("you? ", end="")






# def pattern(n):
#     for i in range(1,n+1):
#         print("*"*(n-i))


# n=int(input("Enter the value of n:"))
# pattern(n)





# def convert(inch):
#     cms=inch*2.54
#     print("The measurements from inches is successfully converted to cms:",cms)

# inch=float(input("Enter the inches:"))
# convert(inch)




# def table(n):
#     for i in range(1,11):
#      print(f"{n} x {i}={n*i}")
        

# n=int(input("enter a number:"))
# table(n)



# def replace(string,word):
#     newstr=string.replace(word,"")
#     return newstr.strip()


# this="    falak is goood     "
# n= replace(this,"falak")
# print(n)
