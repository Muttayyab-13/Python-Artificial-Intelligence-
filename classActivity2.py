import pandas as pd

df = pd.read_csv('./Data Sets/Netflix_dataset.csv')



print(df.head())

import pandas as pd


df.head(10) #1

#2 The data set contains 8807 rows and 12 columns.


df.type.nunique() #3


df.release_year.value_counts() #4 and 5=> Most movies were realeased in 2018 that is = 1147

df[(df['type']=='TV Show') & (df['release_year']==2021)] #6


df[(df['director']=='Kirsten Johnson')] #7


df[(df['country']=='United States') & (df['rating']=='TV-MA')]    #8



df[(df['cast'].str.contains("Samuel Jouy",na=False))]      #9




df[(df['type'] == "Movie") & (df['duration'].str.split(' ', expand=True)[0].astype(float) >= 90)]   #10


df[(df['listed_in'].str.contains("Crime TV Shows",case=False)) & (df['listed_in'].str.contains("International TV Shows",case=False))]     #11

df['date_added'] = pd.to_datetime(df['date_added'],errors='coerce')  

df[
    (df['country'] == 'India') & 
    (df['date_added'] > '2020-01-01')
]       #12


df.sort_values(by='date_added',ascending=True)   #13


 
df.sort_values(by='date_added',ascending=False)      #14  The most recent additionis the Movie=> Dick Johnson Is Dead	Kirsten 


new_dataFrame=df[['title','type','release_year']]          #15
new_dataFrame


df[df['type']=='Movie'].shape[0]   #16  => 6131 Movies


df[df['type']=='TV Show'].shape[0]   #17  => 2676 Shows          



df.groupby('rating')['release_year'].mean().round(1)    #18


df['is_movie']=df['type']=='Movie'  #19
df['is_movie']      #19


df['listed_in'].str.split(', ').explode().str.strip().value_counts()       #20













