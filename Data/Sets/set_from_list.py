def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation: ")
    observation = input
    observations.append(observation)
  
  return observations

def run():
  print("Counting observations...")
  observations = observed()
  observations_set = set()

  for observation in observations:
    occurences = observations.count(observation)
    observations_set.add((observation, occurences))
   
  print(observations_set)

run()