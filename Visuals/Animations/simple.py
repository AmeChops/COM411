#importing the relevant modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#setting global variable
fig, ax = plt.subplots()

#creating function with 1 parameter
def animate(frame):
  #calling global variable  
  global ax

  #setting limits on the x and y axis
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  
  #setting the plots to the current frame number
  ax.plot(frame, frame)

#creating function to run the program
def run():
  
  #calling the global variable
  global fig

  #setting the animation type with frames and intervals
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)

  #ensuring the chart displays
  plt.show()

#calling the function to run the program
run()