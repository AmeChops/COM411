import matplotlib.pyplot as plt

def display(x_values, y_values):
 
  plt.plot(x_values)
  plt.plot(y_values)
  plt.show()

def run():
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  displays = display(x_values, y_values)

  return displays

run()