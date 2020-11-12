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


def phrases(friends):
  quotes = {}

  for friend in friends:
    print(f"What does {friend} say?")
    quote = input()
    quotes[friend] = quote
  
  return quotes

def save(quotes):
  with open("quotes.txt", "w") as file:
    for friend, quote in quotes.items():
      file.write(f"{friend}: {quote}\n")
    

# calling the function with no specified parameter
friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")
save