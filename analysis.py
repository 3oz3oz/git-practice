import numpy as np

# Generate sample dataset (normal distribution)
data = np.random.normal(loc=10, scale=2, size=100)

print(f"Sample Mean: {np.mean(data):.2f}")
print(f"Sample Std Dev: {np.std(data, ddof=1):.2f}")
