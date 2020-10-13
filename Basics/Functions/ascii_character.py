print("Program started!")
print("Please enter an ASCII code")

acode = int(input())

bottom = 32
top = 127

if acode in range(bottom, top):
  letter = chr(acode)
  print("The character represented by the ASCII code {} is {}".format(acode, letter))

else:
  print("The calue entered is outside of the ASCII code range")
  print("Program ended!")