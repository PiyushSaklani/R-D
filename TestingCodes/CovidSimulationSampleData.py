import matplotlib.pyplot as plt

# Sample data
date = ['1/22/20', '1/23/20', '1/24/20', '1/25/20', '1/26/20']
confirmed_cases = [555, 654, 941, 1434, 2118]
deaths = [17, 18, 26, 42, 56]
recoveries = [28, 30, 36, 39, 52]

# Create the plot
plt.plot(date, confirmed_cases, label='Confirmed Cases')
plt.plot(date, deaths, label='Deaths')
plt.plot(date, recoveries, label='Recoveries')

# Add title and axis labels
plt.title('COVID-19 Data')
plt.xlabel('Date')
plt.ylabel('Number of Cases')

# Add legend
plt.legend()

# Show plot
plt.show()
