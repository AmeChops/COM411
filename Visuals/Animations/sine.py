#importing the relevant modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#setting global variable
fig, ax = plt.subplots()

#creating function with 1 parameter
def animate(frame):
  
  #setting limits on the x and y axis
  ax.set_xlim(0, 720)
  ax.set_ylim(-1, 1)

  #setting the values for the x and y axis
  x = np.arange(0, frame)
  y = np.sin(x * np.pi/180)

  #setting the plots to the current frame number and display a red circle marker 
  ax.plot(x, y, 'g')

#creating function to run the program
def run():
  
  #calling the global variable
  global fig

  #setting the animation type with frames and intervals
  sine_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)

  #ensuring the chart displays
  plt.show()

#calling the function to run the program
run()