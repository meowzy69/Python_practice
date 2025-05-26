import matplotlib.pyplot as plt

Task = ['Study', 'Sleep', 'Entertainment', 'Exercise', 'Others']

Data = [4, 8, 4, 2, 3]

colors = ['yellow', 'blue', 'green', 'red', 'purple']

plt.pie(Data, labels=Task, colors=colors, autopct='%1.1f%%')
plt.title('Daily Activities')
plt.legend(title='Activities')
plt.show()

