def phrases():
  friends = ["Scooby Doo", 
             "Shaggy Rogers",
             "Fred Jones",
             "Daphne Blake",
             "Velma Dinkley"]
  
  return friends
  
def run():
  friend_name = phrases()
  
  for freinds in friend_name:
    print("What does {} say?".format(friend_name))
  
run()
   

  

