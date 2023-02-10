#Program 1 for calculating area of a circle
radius=int(input("Enter radius of a circle : "))
area=22/7*radius**2
print("Area of circle with radius ",radius," is :",area)

#Program 2 for naming extension of a file
name=input("Enter a file name with extension")
o=name.split(".")
print(o)
s=o[1]
print(s)
if s == "py":
    print("python file")
elif s == "c":
    print("c file")
elif s == "java":
    print("java file")
elif s == vb:
    print("visual basic file")