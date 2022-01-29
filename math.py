from math.math import plus,kali,minus,floor,pangkat,modulus,bagi

print(r'''
[1] *   [5] %
[2] +   [6] //
[3] -   [7] **
[4] /
''')
math = int(input("[?] Input >>> "))
if math == 1:
      math1 = int(input("(*)>>> "))
      math2 = int(input("(*)>>> "))
      res = kali(math1, math2)
      print("Result :",res)
      
if math == 2:
      math1 = int(input("(+)>>> "))
      math2 = int(input("(+)>>> "))
      res = plus(math1, math2)
      print("Result :",res)
      
if math == 3:
      math1 = int(input("(-)>>> "))
      math2 = int(input("(-)>>> "))
      res = minus(math1, math2)
      print("Result :",res)
      
if math == 4:
      math1 = int(input("(/)>>> "))
      math2 = int(input("(/)>>> "))
      res = bagi(math1, math2)
      print("Result :",res)

if math == 5:
      math1 = int(input("(%)>>> "))
      math2 = int(input("(%)>>> "))
      res = modulus(math1, math2)
      print("Result :",res)
      
if math == 6:
      math1 = int(input("(//)>>> "))
      math2 = int(input("(//)>>> "))
      res = floor(math1, math2)
      print("Result :",res)
      
if math == 7:
      math1 = int(input("(**)>>> "))
      math2 = int(input("(**)>>> "))
      res = pangkat(math1, math2)
      print("Result :",res)
