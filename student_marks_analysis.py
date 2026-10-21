
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Maths": [85, 70, 92, 65, 78],
    "Science": [90, 75, 88, 72, 80],
    "English": [82, 80, 95, 68, 85]
}

df = pd.DataFrame(data)

df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("Student Marks Analysis")
print(df)

print("\nClass Average:", round(df["Average"].mean(), 2))
print("\nTop Performer:")
print(df.loc[df["Total"].idxmax()])

df.plot(x="Student", y="Average", kind="bar", legend=False)
plt.title("Student Average Marks")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()
