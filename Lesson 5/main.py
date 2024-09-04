import matplotlib.pyplot as plt

condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]

fig,(ax1,ax2) = plt.subplots(2,1)

ax1.plot(condition,days)
ax2.plot(condition,days)

plt.pie(days, labels=condition)
plt.title('Weather in Lisbon')
plt.legend(days)
plt.show()
