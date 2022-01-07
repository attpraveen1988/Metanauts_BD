#from itertools import count
#from itertools import count
import pyspark
from pyspark.sql import SparkSession


spark = SparkSession.builder.master("local[1]").appName('SparkByExamples.com').getOrCreate()

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.printSchema()
df.show()

df.createOrReplaceTempView("PERSON_DATA")
df2 = spark.sql("SELECT lastname FROM PERSON_DATA")
df2.printSchema
df2.show()

groupDF = spark.sql("select gender, count(*) from person_data group by gender")
groupDF.show()

df = spark.readStream.format("socket").option("host","localhost").option("port","9090").load()
df.printSchema()

query = count.writeStream.format("console").outputMode("complete").start().awaitTermination()

df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "192.168.1.100:9092").option("subscribe", "json_topic").option("startingOffsets", "earliest").load()

df.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value").writeStream.format("kafka").outputMode("append").option("kafka.bootstrap.servers", "192.168.1.100:9092").option("topic", "josn_data_topic").start().awaitTermination()
