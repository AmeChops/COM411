print("Please enter a whole number")

number = int(input())

if(number % 2 == 0):
  print("{} is even.".format(number))
else:
  print("{} is odd.".format(number))