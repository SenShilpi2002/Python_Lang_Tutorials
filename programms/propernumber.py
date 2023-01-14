n=int(input("Enter a number "))
i , sum = 1 , 0
while(i<n):
    if(n % i == 0):
        print(i)
        sum = sum + i
    i=i+1

print("The sum of the factors : ",sum)        
if(sum == n):
    print("proper")
else:
    print("not proper")