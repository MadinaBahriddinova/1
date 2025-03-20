import matplotlib.pyplot as plt

# Product names and sales data
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Create bar chart
plt.figure(figsize=(7, 5))
plt.bar(products, sales, color=colors)

# Add labels and title
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data for Different Products')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Show the plot
plt.show()
