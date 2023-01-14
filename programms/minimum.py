a=int(input("input 1st number "))
b=int(input("input 2nd number "))
c=int(input("input 3rd number "))


if(a<b and a<c):
    print("a is minimum ")
elif(b<a and b<c):
    print("b is minimum")
else:
    print("c is minimum")