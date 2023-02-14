import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Sample data
date = []
cases = []
deaths = []
recoveries = []

for i in range(100):
    date.append(i)
    cases.append(sum(cases) + random.randint(1000, 10000))
    deaths.append(sum(deaths) + random.randint(100, 1000))
    recoveries.append(sum(recoveries) + random.randint(500, 5000))

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('Date')
ax.set_ylabel('Number of cases')

# Plot data
line1, = ax.plot(date, cases, label='Confirmed cases')
line2, = ax.plot(date, deaths, label='Deaths')
line3, = ax.plot(date, recoveries, label='Recoveries')
ax.legend()

# Animate the graph
def animate(i):
    line1.set_data(date[:i], cases[:i])
    line2.set_data(date[:i], deaths[:i])
    line3.set_data(date[:i], recoveries[:i])
    ax.relim()
    ax.autoscale_view()

ani = animation.FuncAnimation(fig, animate, frames=len(date), repeat=True)
plt.show()
