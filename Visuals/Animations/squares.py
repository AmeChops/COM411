#importing the relevant modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#setting global variable
fig, ax = plt.subplots()
data = []

def init():
  data.append({'x':[3, 3, 4, 4, 3], 'y':[3, 4, 4, 3, 3]})
  data.append({'x':[2, 2, 5, 5, 2], 'y':[2, 5, 5, 2, 2]})
  data.append({'x':[1, 1, 6, 6, 1], 'y':[1, 6, 6, 1, 1]})

#creating function with 1 parameter
def animate(frame):
  #calling the global variable
  global ax
  
  index = frame % len(data)
  ax.cla()
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  ax.plot(data[index]['x'], data[index]['y'])
 
  
#creating function to run the program
def run():
  
  #calling the global variable
  global fig

  #setting the animation type with frames and intervals
  squars_animation = animation.FuncAnimation(fig, animate, frames = 100, interval = 100, init_func = init)

  #ensuring the chart displays
  plt.show()

#calling the function to run the program
run()