#Program for Fibonacci numbers
n = int(input("Enter the value for 'n' number : "))
a = 0
b = 1
sum = 0
for i in range(0,n) :
        print(sum)
        a = b
        b = sum
        sum = a + b