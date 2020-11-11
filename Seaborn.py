#Seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
a=sns.load_dataset("flights")
sns.relplot(x="passengers",y="month",hue='year',data=a)
#exp2
b=sns.load_dataset("tips")
sns.relplot(x="time",y="tip",data=b,kind="line")
#exp3
sns.catplot(x="day",y="total_bill",data=b)
#exp4
sns.catplot(x="day",y="total_bill",kind='violin',data=b)
#exp5
sns.catplot(x="day",y="total_bill",kind='boxen',data=b)
#exp6
sns.catplot(x="day",y="total_bill",kind='box',data=b)
#exp7 using uni variat
from scipy import stats
c=np.random.normal(loc=5,size=100,scale=2)
sns.distplot(c)
#exp8 using bivariat
a=sns.load_dataset("iris")
b=sns.FacetGrid(a,col="species")
b.map(plt.hist,"sepal_length")
#exp9
a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)
#exp10
#Plot Aesthetics
sns.set(style="darkgrid") #
a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)
#exp11
sns.set(style="white",color_codes=True)
a=sns.load_dataset("tips")
sns.boxplot(x="day",y="total_bill",data=a)
sns.despine(offset=10,trim=True)
#exp12
c=sns.color_palette()
sns.palplot(c)

