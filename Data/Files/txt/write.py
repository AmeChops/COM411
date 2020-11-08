def search(filename):

  print("Searching...", end = "")

  print("Searching...")

  sections = []
  books = []
  
  with open(filename) as file:
    for line in file:
      if line.startswith("Section"):
        split = line.split(":")
        sections.append(split[1][:-1])
      else:
        books.append(line[:-1])
  
  print("Done!")
  data = (sections, books)

  return data

def save(filename, data):

  print("Saving...", end = "")

  with open(filename, "w") as file:
    file.write("Sections: ")
    for index in range(len(data[0])):
      if (index < len(data[0]) -1):
        file.write(f"{data[0][index]}, ")
      else:
        file.write(f"{data[0][index]}")

    file.write("\nBooks: ")
    for element in data[1]:
      file.write(f"{element}, ")

  print("Saving...")

  with open(filename, "w") as file:
    file.write("Sections: ")
    for element in data[0]:
      file.write(element + ", ")

    file.write("\nBooks: ")
    for element in data[1]:
      file.write(element + ", ")

    print("Done!")

def run():
  data = search("Data/Files/txt/books.txt")
  save("Data/Files/txt/sections_books.txt", data)
  
run()
