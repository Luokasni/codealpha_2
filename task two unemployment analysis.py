import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Loga\Downloads\Unemployment in India.csv")


# Clean column names
df.columns = df.columns.str.strip()

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"].str.strip(), format="%d-%m-%Y")

# Drop missing values
df.dropna(inplace=True)

# Overview of data
print(df.info())
print(df.head())

# 📌 Plot: Unemployment Rate Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Date", y="Estimated Unemployment Rate (%)", ci=None, marker="o", color="b")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.title("Unemployment Rate Trend in India")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 📌 Bar Chart: State-wise Unemployment Rate (Average)
plt.figure(figsize=(14, 6))
statewise_unemp = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values(ascending=False)
sns.barplot(x=statewise_unemp.index, y=statewise_unemp.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.xlabel("States")
plt.ylabel("Avg. Unemployment Rate (%)")
plt.title("State-wise Average Unemployment Rate")
plt.show()

# 📌 Boxplot: Urban vs Rural Unemployment
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Area", y="Estimated Unemployment Rate (%)", palette=["orange", "green"])
plt.xlabel("Area Type")
plt.ylabel("Unemployment Rate (%)")
plt.title("Urban vs Rural Unemployment Rate Distribution")
plt.show()

# 📌 Heatmap: Correlation between Employment, Labour Participation, and Unemployment
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Area", y="Estimated Unemployment Rate (%)", hue="Area", 
            palette=["orange", "green"], legend=False)
plt.title("Correlation Heatmap")
plt.show()
