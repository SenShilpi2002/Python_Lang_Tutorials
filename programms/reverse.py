n=int(input("Enter a number "))
digit,ans=0,0
while(n!=0):
    digit=n%10
    ans=(ans*10)+digit
    n= n//10
print("The ans is: ",ans)




