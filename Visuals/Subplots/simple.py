import matplotlib.pyplot as plt

def read_data(file_path):
  temps = []
  file = open(file_path)
  lines = file.readlines()
  for line in lines:
    temps.append(line.strip())
  file.close()
  return temps
 
def run():
  data = read_data("Visuals/Subplots/temps.txt")
  fig, axes = plt.subplots(2,2)
  axes[0,0].plot(data)
  plt.show()
  
run() 