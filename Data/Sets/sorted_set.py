def observed():
  observations = []
  for count in range(5):
    print("Please enter a value:")
    item = input()
    observations.append(item)

  return observations

def remove_observations(observations):
  is_running = True

  while(is_running):
    print("do you wish to remove and observation (yes/no)?")
    answer = input()

    if (answer == "yes"):
      print("Waht would you like to remove?")
      to_remove = input()
      observations.remove(to_remove)
    else:
      is_running = False
    
def run():
  observations = observed()
  remove_observations(observations)

  observations_set = set()
  
  for observation in observations:
    occurences = observations.count(observation)
    observations_set.add((observation, occurences))
  
  for key, value in sorted(observations_set):
    print("{key} observed {value} times.")

run()
