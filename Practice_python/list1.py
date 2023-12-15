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
# Check list is empty or not

lis = []

if lis:
    print("List is not empty")  
else:
    print("List is empty")

print("***********************************")

# Remove duplicates

a = [1, 1, 2, 3, 4, 5, 6, 7, 1, 8, 9, 10]

z = set(a)
print(list(z))

# Smallest number from list
print("*******************************")
#1
a = [1, -1, 2, 3, 4, 5, 6, 7, 1, 8, 9, 10]
print(min(a), max(a), "\n\n")
#2
smallest_number = None
for number in a:
    if smallest_number is None or number < smallest_number:
        smallest_number = number

print(smallest_number)
#3
larg_num = None
for num in a:
    if larg_num is None or num > larg_num:
        larg_num = num

print(larg_num)


# Get a string made of the first 2 and the last 2 chars from a given a string

print("*******************************")

a = "Hari"
#print(len(a))
if len(a) < 2:
    print("Empty string")
else:
    print(a[0:2], a[-2:])

print("*******************************")

# Sum of elements
# Mulitply of elements

a = [1, 1, 1, 1, -5]
z = 0
for n in a:
    if n:
        z = z + n
print(z)

for n in a:
    if n:
        z = z * n
print(z)

print("*******************************")
#  Clone or copy
a= ["hari"]
print(a)
z = a.copy()
print(z)

print("***********************************")

def by_length(fruit):
  return len(fruit)

fruits = ['apple', 'orange', 'banana', "hh", "njh"]
fruits.sort(key = by_length)
print(fruits)



