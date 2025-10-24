import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

cmap=sns.cubehelix_palette(dark=0.3, light=.8, as_cmap=True)
# sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", palette=cmap, data=tips)
# sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", sizes=(20, 200), palette=cmap, legend="full", data=tips)
# sns.scatterplot(x="total_bill", y="tip", hue="day", size="smoker", palette="Set2", sizes=(20, 200), legend="full", data=tips)
# sns.scatterplot(x="total_bill", y="tip", s=100, color=".2", marker="+", data=tips)
sns.scatterplot(x=iris.sepal_length, y=iris.sepal_width, hue=iris.species, style=iris.species)
plt.show()