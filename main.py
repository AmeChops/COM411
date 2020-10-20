# setting up the function with no parameters 
def myth():
  # displaying initial message
  print ("Who wishes to learn about the demidog Maui?")  

  # reading and storing user's response to question above
  user_name = input()

  # displaying the story message inserting the users input from previous step
  print("Well, {}, he stole the heart of the goddess Te Fiti.".format(user_name))

  # displaying the final message here (requirement 5 above)
  print("You must find Maui and lift the curse!")

# calling the function with no specified parameter as it is being read from the users input above
myth()