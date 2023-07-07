import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from accelerometer_comm import getRollPitch

COM_PORT = 'COM10'

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from accelerometer_comm import getRollPitch

# Parameters
x_len = 200         # Number of points to display
y_range = [-90, 90]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)


# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('Roll & Pitch')
plt.xlabel('Samples')
plt.ylabel('Pitch')

# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read temperature (Celsius) from TMP102
    r, p = getRollPitch(COM_PORT)

    # Add y to list
    ys.append(r)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=50,
    blit=True)
plt.show()