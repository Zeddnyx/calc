from math.math import plus,kali,minus,floor,pangkat,modulus,bagi

rpt = 1

while rpt == 1:

 print(r'''
 [1] *   [5] %
 [2] +   [6] //
 [3] -   [7] **
 [4] /
 ''')
 math = int(input("[?] Input >>> "))
 if math == 1:
      math1 = float(input("(*)>>> "))
      math2 = float(input("(*)>>> "))
      res = kali(math1, math2)
      print("Result :",res)
      
 if math == 2:
      math1 = float(input("(+)>>> "))
      math2 = float(input("(+)>>> "))
      res = plus(math1, math2)
      print("Result :",res)
      
 if math == 3:
      math1 = float(input("(-)>>> "))
      math2 = float(input("(-)>>> "))
      res = minus(math1, math2)
      print("Result :",res)
      
 if math == 4:
      math1 = float(input("(/)>>> "))
      math2 = float(input("(/)>>> "))
      if math1 and math2 >  0:
       res = bagi(math1, math2)
       print("Result :",res)
      else:
       print("Impossible!")

 if math == 5:
      math1 = float(input("(%)>>> "))
      math2 = float(input("(%)>>> "))
      res = modulus(math1, math2)
      print("Result :",res)
      
 if math == 6:
      math1 = float(input("(//)>>> "))
      math2 = float(input("(//)>>> "))
      if math1 and math2 >  0:
       res = bagi(math1, math2)
       print("Result :",res)
      else:
       print("Impossible!")
      
 if math == 7:
      math1 = float(input("(**)>>> "))
      math2 = float(input("(**)>>> "))
      res = pangkat(math1, math2)
      print("Result :",res)

 stp = input("""Stop? Y/N: """)
 if stp == "Y":
       exit()
 
