n=int(input("Enter a number "))
digit , ans = 0,0
t=n
while(n!=0):
    digit = n % 10
    ans = ans+(digit**3)
    n = n//10
if(ans==t):
    print("The number is armstrong ")
else:
    print("The number is not armstrong ")