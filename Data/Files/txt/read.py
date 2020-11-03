def search(filename):
  print("Searching...")
  
  with open(filename) as file:
    for line in file:
      lines = file.read().split('\n')
      for line in lines:
        print(f"Looked in {line}.")
  
  print("...Done!")

def run():
  search("Data/Files/txt/locations.txt")
    
run()
 