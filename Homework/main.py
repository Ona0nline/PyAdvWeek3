import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

fig,(ax1,ax2) = plt.subplots(1,2)

ax1.plot(years,temp_anomalies,label="Temperature anomalies",color="r")
ax1.set_title("temperature anomalies over the years")
ax1.legend(temp_anomalies)


ax2.bar(years,co2_emissions,label="CO2 emissions")
ax2.set_title("CO2 emissions over the years")
ax1.legend(co2_emissions)


plt.tight_layout()
plt.show()