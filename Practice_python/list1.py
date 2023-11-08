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
