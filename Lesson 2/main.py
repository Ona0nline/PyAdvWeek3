import matplotlib.pyplot as plt

lisbon_temperatures = [25, 26, 28, 24, 22]
new_york_temperatures = [15, 17, 12, 20, 22]
sydney_temperatures = [10, 12, 11, 8, 7]

days = ['Monday', 'Tuesday', 'Wednesday', "Thursday", 'Friday']

# Styling

print(plt.style.available)
plt.style.use('Solarize_Light2')
plt.grid(True)

plt.plot(days, lisbon_temperatures, linewidth=4,color='r')
plt.plot(days, new_york_temperatures,color='g',linestyle="-.")
plt.plot(days, sydney_temperatures,linewidth=3,color='b')

plt.legend(['Lisbon', 'New York', 'Sydney'])

plt.xlabel("Days")
plt.ylabel("Temperatures (in celcius)")

plt.title("Weather forecast")


plt.show()



