import sys
#print(sys.argv[1])


#
num1 = sys.argv[1]
choice = sys.argv[2]
num2 = sys.argv[3]



if choice == "-":
      print(int(num1)-int(num2))
elif choice == "+":
      print(int(num1)+int(num2))