# Get a string made of the first 2 and the last 2 chars from a given a string
n= "Hariprakash"
def str1(a):    
    n = a[0] + a[1] + a[-2] + a[-1  ]
    print(n)

str1("Hariprksh")           
print("***********************************")
def printbothends(str1):
  if len(str1) < 2:
    print("..")
    return ""
  else:
    return str1[0:2] + str1[-2:]

sta = "hariiii"
print(printbothends(sta))
