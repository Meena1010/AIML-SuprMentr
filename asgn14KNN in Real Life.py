# 1. KNN in Real Life
# Explanation:

# KNN (K-Nearest Neighbors) works by finding similar users or items. Netflix uses it by comparing your watch history with others and recommending content liked by similar users.

# Example Code:
from sklearn.neighbors import NearestNeighbors
import numpy as np

data = np.array([
    [5, 4],
    [4, 5],
    [1, 2],
    [2, 1]
])

model = NearestNeighbors(n_neighbors=2)
model.fit(data)

new_user = np.array([[5, 5]])
distances, indices = model.kneighbors(new_user)

print("Nearest Neighbors Index:", indices)
print("Distances:", distances)