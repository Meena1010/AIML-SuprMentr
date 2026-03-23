import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "Income": [15, 16, 17, 18, 90, 92, 95, 100],
    "Spending": [39, 40, 42, 43, 81, 83, 85, 88]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=2, random_state=0)
df["Cluster"] = kmeans.fit_predict(df)

plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()

print(df)