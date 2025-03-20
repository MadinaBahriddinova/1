import numpy as np
import matplotlib.pyplot as plt

# Time periods and categories
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [3, 5, 2, 6]
category_B = [4, 3, 5, 2]
category_C = [2, 4, 3, 5]

# Stacked bar chart
plt.figure(figsize=(7, 5))
plt.bar(time_periods, category_A, color='blue', label='Category A')
plt.bar(time_periods, category_B, color='green', bottom=category_A, label='Category B')
plt.bar(time_periods, category_C, color='red', bottom=np.array(category_A) + np.array(category_B), label='Category C')

# Add labels and title
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')

# Add legend
plt.legend()

# Show the plot
plt.show()
