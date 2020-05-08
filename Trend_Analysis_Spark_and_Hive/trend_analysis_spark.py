#Spark Python Code to perform Trend Analysis.
import pyspark
import time
from pyspark.sql import Row

#Read the file from HDFS.
data=sc.textFile("./desktop/twitter/covid_data_day*")

#Start initial Time
time1 = time.time()

#Split the Data
data_split=data.flatMap(lambda x:x.split(" "))

#Filter only the hashtags from the data.
hashtags=data_split.filter(lambda x:"#" in x)

#Assign a tuple value of key-value pair(x,1) to all elements to calculate number of similar tweets.
tweet=hashtags.map(lambda x:(x,1))

#Since RDD has a tuple of key-value pair =(tweet,1) , add all the values with similar keys.
add=tweet.reduceByKey(lambda x,y:x+y)

#set the count in the decreasing order to retrieve only the most popular tweets.
list=add.map(lambda x:(x[1],x[0]))

desc=list.sortByKey(ascending=False)

#Now the RDD has a key-value pair of key as tweet with value of total counts.
#create a Dataframe to run queries
df=desc.map(lambda x:Row(tweet_count=x[0],tweet=x[1]))

df=df.toDF()

#register the dataframe as a View table to run SQL queries
df.createOrReplaceTempView('table')

#now query the data using sparkSQL
query=spark.sql("SELECT * FROM table limit 10")

#now there might be few incorrect hastags in the table , so retreive only the proper tweets
result=spark.sql("SELECT * FROM table WHERE table.tweet LIKE '#%'")
time2 = time.time()
print(time2 - time1)

#display the results
result.show() 

