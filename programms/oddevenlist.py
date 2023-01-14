l=list(eval(input("Enter a list")))
l1=list()
l2=list()
for i in range(0,len(l)):
    if(l[i]%2 == 0):
        l1.append(l[i])
    else:
        l2.append(l[i])

l1.sort()
l2.sort()

print("The even list :",l1)
print("The odd list :",l2)
