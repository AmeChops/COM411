def search(filename):
  print("Searching...")
  
  with open(filename) as file:
    for line in file:
<<<<<<< HEAD
      lines = file.read().split('\n')
      for line in lines:
        print(f"Looked in {line}.")
=======
      print(f"Looked in the {line}")
>>>>>>> fbccaac756b6da3b826f692dda64c73734ec6624
  
  print("...Done!")

def run():
  search("Data/Files/txt/locations.txt")
    
run()
 