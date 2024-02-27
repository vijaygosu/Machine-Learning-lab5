import numpy as np
import matplotlib.pyplot as plt

# Generate 20 data points with 2 features (X & Y) randomly varying between 1 and 10
np.random.seed(0)  # For reproducibility
X = np.random.randint(1, 11, size=(20, 2))  # Random values between 1 and 10
print("Generated data points:")
print(X)

# Assign these 20 points to 2 different classes (class 0 - Blue & class 1 – Red)
y = np.random.randint(0, 2, size=20)  # Randomly assign class labels (0 or 1)
print("Assigned class labels:")
print(y)

# Separate points for each class
class0 = X[y == 0]
class1 = X[y == 1]

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(class0[:, 0], class0[:, 1], color='blue', label='Class 0')
plt.scatter(class1[:, 0], class1[:, 1], color='red', label='Class 1')

# Set plot labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Training Data')

# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()
