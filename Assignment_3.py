#Program to print all positive numbers in a range.
l_num=[]
neg=[]
ans=int(input("Enter how many numbers do you want in list : ))
i=1
while i <= ans:
    num=int(input("Enter number : "))
    l_num.append(num)
    i+=1
for j in l_num:
    if j >= 0:
        continue
    else:
        neg.append(j)
if len(neg)==0:
    print("There is no negative in the list of numbers")
else:
    print("List of negative numbers : ",neg)