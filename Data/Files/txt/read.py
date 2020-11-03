def search(filename):
  print("Searching...")
  
  with open(filename) as file:
    for line in file:
      print(f"Looked in the {line}\n")
  
  print("Done!")

def run():
  location = search("Data/Files/txt/locations.txt")
  return location
  
run()
