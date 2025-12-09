import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("new_roller_coaster.csv")
ax=df["Year_Introduced"].value_counts().head(10).plot(kind="bar",title="Top 10 Years of Roller Coasters Introduced")
ax.set_xlabel("Year Introduced")
ax.set_ylabel("Count")
plt.show()