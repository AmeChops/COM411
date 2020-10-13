# The function
def escape_by():
  print("How will we escape? 1 - Jump over, 2 - Run around, 3 - Go deeper")
  plan = int(input())

 # The parameters 
  if plan == 1:
   print("We cannot escape by jumping over, the boulder is too big")
  elif plan == 2:
   print("We cannot escape by running around, the boulder is moving too fast")
  elif plan == 3:
   print("That might just work, let's go deeper")
    
# Call the function
escape_by()


