#importing the relevant modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#setting global variable
fig, ax = plt.subplots()

#creating function with 1 parameter
def animate(frame):
  #calling the global variable
  global ax
  
  #clearing the current axes
  ax.cla()

  #setting limits on the x and y axis
  ax.set_xlim(0, 2 * np.pi)
  ax.set_ylim(-1, 1)

  #setting the values for the x and y axis
  x = np.arange(0, 2 * np.pi, 0.01)
  y = np.sin(x + frame / 50)

  #setting the plots to the current frame number and display a green marker 
  ax.plot(x, y, 'g')

#creating function to run the program
def run():
  
  #calling the global variable
  global fig

  #setting the animation type with frames and intervals
  shift_sine_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 10)

  #ensuring the chart displays
  plt.show()

#calling the function to run the program
run()