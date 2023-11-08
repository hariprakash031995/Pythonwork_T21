# Count no of strings whose length is 2

name = ["hari", "John", "arun", "le", "don", "a"]

for n in name:
    if len(n)==2:
        print(n, "This is two digit length")

    # else:
    #     print(n, "is not a 2 digit string")


print("***********************************")

name.pop(0)
print(name)

print("***********************************")
# First,Last elements whose square value is between 1 and 30

def square(n):
    if n >= 1 and n <= 30:
        return n ** 2 
    else:
        return 0 
    
print(square(100))

print("***********************************")

# Clone or copy

a = [1, 2, 3]
b = a.copy()
print(a)
print(b)

print("***********************************")
a= [1,2,3]
b=a.copy()
print(a)
print(b)

print("***********************************")
