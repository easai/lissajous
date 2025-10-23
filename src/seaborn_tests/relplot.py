import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
tips=sns.load_dataset("tips")
# sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)
# sns.relplot(x="total_bill", y="tip", size="size", data=tips)
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15,200),data=tips)
# sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-5,l=.75", data=tips)
plt.show()