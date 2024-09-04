import matplotlib.pyplot as plt

condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]

plt.pie(days,labels=condition)
plt.ylabel("Conditions")
plt.title("Number of days with these conditions")
plt.show()
