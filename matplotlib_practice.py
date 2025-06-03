import matplotlib.pyplot as plt

Task = ['Study', 'Sleep', 'Entertainment', 'Exercise', 'Others']

Data = [4, 8, 4, 2, 3]

colors = ['yellow', 'blue', 'green', 'red', 'purple']

plt.pie(Data, labels=Task, colors=colors, autopct='%1.1f%%')
plt.title('Daily Activities')
plt.legend(title='Activities')
plt.clf()  # Clear the current figure


#Subplots and multiple graphs

# Side by side line and bar chart
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 35] #line
y2 = [5, 15, 20, 25, 30] #bar

#line plot 1st subplot
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.plot(x, y1, color='blue')
plt.title('Line Chart')

#bar plot 2nd subplot
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.bar(x, y2, color='orange')
plt.title('Bar Chart')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plots


# 2 rows, 2 columns , 4 charts

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(figsize=(10, 6)) 

#line
plt.subplot(2, 2, 1)
plt.plot(x, y, color='blue')
plt.title('Line Chart')

#bar
plt.subplot(2, 2, 2)
plt.bar(x, y, color='orange')
plt.title('Bar Chart')

#scatter
plt.subplot(2, 2, 3)
plt.scatter(x, y, color='green')
plt.title('Scatter Plot')

#pie
plt.subplot(2, 2, 4)
labels = ['A', 'B', 'C', 'D']
plt.pie(y, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.tight_layout()  
plt.show()  
plt.clf()  # Clear the current figure

# Challenge : Creating three subplots on 1 row

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.figure(figsize=(15, 5))  # line

plt.subplot(1, 3, 1)
plt.plot(x, y, color='blue')
plt.title('Line Chart')

# bar
plt.subplot(1, 3, 2)
plt.bar(x, y, color='orange')
plt.title('Bar Chart')

# scatter
plt.subplot(1, 3, 3)
plt.scatter(x, y, color='green')
plt.title('Scatter Plot')

plt.tight_layout()  
plt.show()  


# Learning to style the plots

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.figure()
plt.plot(x, y, color = 'green', linestyle='--', linewidth=2, marker='o', markersize=8) 
plt.title('Styled Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()  