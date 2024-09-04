import matplotlib.pyplot as plt

Lisbon_forecast = [12,13,15,18,23]
new_york_forecast = [2,4,3,6,16]
sydney_forecast = [22,25,23,27,34]
index = ["Thurs","Fri","Sat","Sun","Mon"]

plt.plot(Lisbon_forecast)
plt.plot(new_york_forecast)
plt.plot(sydney_forecast)

plt.legend(['Lisbon','New York','Sydney'])
plt.title("Temperature forecast (5 days)")
plt.xlabel('Next 5 days')
plt.ylabel('Temperature in degrees celsius')

plt.show()

plt.savefig('population_plot.png')
