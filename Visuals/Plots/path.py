import matplotlib.pyplot as plt

def coordinate():
  x = input("Please enter an X value")
  y = input("Please enter a Y value")
  x_and_y_values = (x, y)

  return x_and_y_values

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []

  for i in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  
  return [x_values, y_values]

def run():
  values = path()
  plt.plot(values[0], values[1], "ro--")
  plt.show()

run()