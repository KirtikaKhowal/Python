"""
Title: Weather Data Visualizer
Author: Kirtika Khowal
Roll No.-2501730285
Date: 2025-11-23
Section--B
Description: In this assignment, we loaded real weather data from a CSV file and performed data cleaning, processing, and statistical analysis using Pandas and NumPy.
We visualized temperature, rainfall, and humidity trends using Matplotlib and created grouped insights by month and season. 
Finally, we exported the cleaned dataset and summarized our findings in a report.
"""


import pandas as pd


df = pd.read_csv("https://storage.googleapis.com/kagglesdsdata/datasets/6883/9923/weather.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20251123%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251123T130443Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=04cf92c4f03d3dbfaa82072a585cf108c4a2cf147958123a97966cbdeac6fa71dece3842e3a86dd88004acf9720041a1894e209a07976725a31512e03115c228d9ffe83bee35fdba30bfd1d8e65d2978bafaec766c5c2e9004b044227ed91aaa18ca7047b24d87da30d6ad07fc52499263b9c2d029ef94beaa78195448883b9e94a5538825cfc20fadf028bd870ca880c9514fb7506a7e6f946dae10194ac2390d42bdd6e329a8bde07dc6787c2aca964419be32b5533e84f11630a9c31202b344b70cc4a476582abb67a0585f5c6a93a68555578dfc7c326ea462c52ae1c7e6636e15f6fbb1e9970f0c81ae83852c84fc6dbc8a02198839a199143d911f7544")


print("\n--- HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())

import numpy as np

date_col = [c for c in df.columns if 'date' in c.lower()][0]
df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].mean())


keep_cols = [date_col] + [c for c in df.columns if any(x in c.lower() for x in ["temp","rain","humid"])]
df_clean = df[keep_cols]

print("\nCleaned Data Preview:\n", df_clean.head())

df_clean = df_clean.set_index(date_col)

daily_stats = df_clean.resample("D").mean()
monthly_stats = df_clean.resample("M").mean()
yearly_stats = df_clean.resample("Y").mean()

print("\nDaily Stats:\n", daily_stats.head())
print("\nMonthly Stats:\n", monthly_stats.head())
print("\nYearly Stats:\n", yearly_stats)

import matplotlib.pyplot as plt


temp_col = [c for c in df_clean.columns if "temp" in c.lower()][0]
plt.plot(df_clean.index, df_clean[temp_col])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()


rain_col = [c for c in df_clean.columns if "rain" in c.lower()][0]
monthly_rain = df_clean[rain_col].resample("M").sum()
monthly_rain.plot(kind="bar", title="Monthly Rainfall")
plt.show()


humid_col = [c for c in df_clean.columns if "humid" in c.lower()][0]
plt.scatter(df_clean[temp_col], df_clean[humid_col])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.show()


plt.figure(figsize=(10,5))
plt.plot(df_clean.index, df_clean[temp_col], label="Temperature")
plt.twinx()
plt.bar(df_clean.index, df_clean[rain_col], alpha=0.3, label="Rainfall")
plt.title("Temperature + Rainfall Combined")
plt.show()

monthly_group = df_clean.resample("M").agg(["mean","max","min"])
print("\nMonthly Grouped Data:\n", monthly_group.head())

season_map = {12:"Winter",1:"Winter",2:"Winter",
              3:"Spring",4:"Spring",5:"Spring",
              6:"Summer",7:"Summer",8:"Summer",
              9:"Autumn",10:"Autumn",11:"Autumn"}

df_clean["season"] = df_clean.index.month.map(season_map)

season_group = df_clean.groupby("season").mean()
print("\nSeasonal Summary:\n", season_group)

df_clean.to_csv("https://chatgpt.com/backend-api/estuary/content?id=file_00000000a490720792600fc348e4dfc1&ts=489973&p=fs&cid=1&sig=6182b8331eadc4cb4ef355cb82bff4d86228da49f25ac6d2fc5f11da9f4ccffc&v=0", index=True)

plt.savefig("plot_name.png")

with open("weather_report.md","w") as f:
    f.write("# Weather Analysis Report\n")
    f.write("## Summary\nThis report covers cleaning, statistics, and plots.\n")



