import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
ss=SparkSession.builder.master("local[1]").appName("march").getOrCreate()
df1=ss.read.csv("/home/harikrishnan/Downloads/Hive_Joining/custom.txt",sep=',',header=None,inferSchema=True)
df2=ss.read.csv("/home/harikrishnan/Downloads/Hive_Joining/order.txt",sep=',',header=None,inferSchema=True)

df3=df1.withColumnRenamed("_c0","Id").withColumnRenamed("_c1","name") \
    .withColumnRenamed("_c2","age").withColumnRenamed("_c3","location") \
    .withColumnRenamed("_c4","salary")
df4 = df2.withColumnRenamed("_c0","oid").withColumnRenamed("_c1","dat") \
    .withColumnRenamed("_c2","Id").withColumnRenamed("_c3","amount")


df5 = df3.join(df4,df3.Id==df4.Id,'inner')


#name,age,loc,dat,amount
#salary above 2000 name,age,loc,dat,amount
#age mxm 1 employee name,age,loc,salary,dat,amount
#latest dat name,age,loc,salary,dat,amount

df6 = df5.select("name","age","location","dat","amount")
df6.show()
print("*"*100)
df7 = df5.filter(col("salary")>2000).select("name","age","location","dat","amount")
df7.show()
print("*"*100)
df8 = df5.orderBy("age",ascending=False).select("name","age","location","salary","dat","amount")
df8.show(1)
print("*"*100)
df9 = df5.orderBy("dat",ascending=False).select("name","age","location","dat","amount")
df9.show()