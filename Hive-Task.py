import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName('SparkByExamples1.com').getOrCreate()

df = spark.read.csv("hdfs://localhost:9000/user/data/test.csv")
df.show()

#df.groupBy("Emp ID").max("Salary")
df.select(df.columns[0:3])
df.show()
df.write.format("orc").saveAsTable("newdf")