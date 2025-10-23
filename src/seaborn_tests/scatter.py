import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.set(style="darkgrid")
# sns.scatterplot(x="total_bill", y="tip", data=tips)
# sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)
# sns.scatterplot(x="total_bill", y="tip", hue="time", style="time", data=tips)
# sns.scatterplot(x="total_bill", y="tip", hue="day", style="time", data=tips)
# sns.scatterplot(x="total_bill", y="tip", size="size", data=tips)
sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", data=tips)
plt.show()