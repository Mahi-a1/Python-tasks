import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in iris dataset from seaborn
df = sns.load_dataset("iris")

# Display first few rows
print(df.head())
# Check dataset structure
print(df.info())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
avg_petal_length = df['petal_length'].mean()
print(f"Average Petal Length: {avg_petal_length:.2f}")
avg_by_species = df.groupby("species")["petal_length"].mean()

avg_by_species.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Petal Length by Species")
plt.ylabel("Average Petal Length (cm)")
plt.xlabel("Species")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species', palette='Set2')
plt.title("Petal Length vs Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
