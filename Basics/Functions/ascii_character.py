print("Program started!")
print("Please enter an ASCII code")

acode = abs(int(input()))

if (acode >= 32 and acode <= 126):
  letter = chr(acode)
  print("The character represented by the ASCII code {} is {}".format(acode, letter))

else:
  print("The value entered is outside of the ASCII code range")

print("Program ended!")