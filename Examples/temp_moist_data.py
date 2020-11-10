# Load temperature or moisture data

import matplotlib.pyplot as plt

def load_temperature_data():
  temps = [10, 20, 18, 19, 5]
  return temps

def load_moisture_data():
  moisture = [20, 40, 30, 15, 12]
  return moisture

def display(data):
  plt.plot(data[0])
  plt.plot(data[1])
  plt.show()

def save(data):
  with open('output.txt') as file:
    temps = data[0]
    moistures = data[1]

    for temp in temps:
      file.write(f"{temp},")
    
    file.write("\n")

    for moisture in moistures:
      file.write(f"{moisture},")

temps = load_temperature_data()
moisture = load_moisture_data()

display([temps, moisture])
display([temps, moisture])