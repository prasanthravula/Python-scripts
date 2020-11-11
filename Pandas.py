import pandas as pd
xyz_web={'Day':[1,2,3,4,5,6],'Visitors':[1000,700,6000,1000,400,350],"Bounce_Rate":[20,20,25,15,10,34]}
df=pd.DataFrame(xyz_web)
print(df)
#Pandas Operations
#Slicing the DataFrame
print(df.head(2))
print(df.tail(2))
#Joining and merging
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2001,2001,2003,2004])
df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2005,2006,2007,2008])
merge=pd.merge(df1,df2)
print(merge)
print(pd.merge(df1,df2, on ="HPI"))
#Joining
import pandas as pd
df1=pd.DataFrame({"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"Low_Tier_HPI":[80,90,70,60],"Uneemployment":[2,1,2,3]},index=[2001,2003,2004,2005])
join=df1.join(df2)
print(join)
#Changing The Index
import pandas as pd
df=pd.DataFrame({"Day":[1,2,3,4],"visitors":[200,100,230,300],"Bounce_rate":[20,45,60,10]})
print(df)
df.set_index("Day",inplace=True)
print(df)
#changing the column headers
df=df.rename(columns={"visitors":"Users"})
print(df)
#concatination
import pandas as pd
df4=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2001,2001,2003,2004])
df5=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2005,2006,2007,2008])
print(pd.concat([df4,df5]))
#Data Munging
#to covrt csv to html dbd exp
#Statistices in python
from statistics import mean,median,mode,variance
print(mean([1,2,3,4,5,6,1,2,3,7,8,9]))
print(median([1,2,3,4,5,6,1,2,3,7,8,9]))
print(mode([1,2,3,4,5,6,1,2,3,7,8,9,2]))
print(variance([1,2,3,4,5,6,1,2,3,7,8,9]))
#python for Hadoop




