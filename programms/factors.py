n=int(input("Enter a number "))

i=1
print("The factors are : ")
while(i<n):
    if(n % i == 0):
        print(i)
    i=i+1

