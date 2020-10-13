print("Program started!")

print("Please enter a standard character")

letter = input()


if len(letter) > 1:
  print("enter 1 character only")

else:
  print("The letter", letter, "as ASCII code is {}".format(ord(letter)))

print("Program ended!")