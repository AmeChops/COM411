def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return(directions)

def menu():
  print ("Please select a direction")
  direction = directions()

  for index in range(len(direction)):
    print("{}: {}".format(int(index), direction[index]))

menu()