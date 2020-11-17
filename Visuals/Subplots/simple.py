import matplotlib.pyplot as plt

def read_data(filepath):
  with open(filepath) as file:
    temperatures = []
    for line in file:
      temperature = float(line.strip())
      temperatures.append(temperature)

  return temperatures

def run():
  data = read_data('Visuals/Subplots/temps.txt')
  fig, (ax1, ax2) = plt.subplots(1, 2)

  ax1.plot(range(1, 8), data)
  ax2.bar(range(1, 8), data)
  plt.tight_layout()
  plt.show()

run()