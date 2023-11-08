# Count no of strings whose length is 2

name = ["hari", "John", "arun", "le", "don", "a"]

for n in name:
    a = 2 <= len(n) < 3
    if a is True:
        print(n)
    