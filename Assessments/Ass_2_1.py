# setting up the function with no parameters
def gang():
  
  # displaying initial message
  print("Loading gang...")
  
  # creating list called 'friends'
  friends = []
  
  # populating list called 'friends'
  friends.append("Scooby Doo")
  friends.append("Shaggy Rogers")
  friends.append("Fred Jones")
  friends.append("Daphne Blake") 
  friends.append("Velma Dinkley")

  # displaying the contents of the list 'friends' with final message
  print(friends, "\n...Done!")
  return friends()

# calling the function with no specified parameter
gang()
