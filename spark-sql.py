from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create a SparkSession
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

def mapper(line):
    fields = line.split(',')
    return Row(ID=int(fields[0]), name=str(fields[1].encode("utf-8")), age=int(fields[2]), numFriends=int(fields[3]))

lines = spark.sparkContext.textFile("fakefriends.csv")
print(f'\ntype(lines): {type(lines)}') # type(lines): <class 'pyspark.core.rdd.RDD'>
people = lines.map(mapper)
print(f'\ntype(people): {type(people)}') # type(people): <class 'pyspark.core.rdd.PipelinedRDD'>

# Infer the schema, and register the DataFrame as a table.
# for next 2 lines -
# 1. pehli line me upar jo "people" RDD bani hai, usey paas karke dataframe banare.
# 2. second line me uss dataframe ko as table register karre (aur naam people rakh liya)
schemaPeople = spark.createDataFrame(people).cache()
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
teenagers = spark.sql("SELECT * FROM people WHERE age >= 13 AND age <= 19")

# The results of SQL queries are RDDs and support all the normal RDD operations.
for teen in teenagers.collect():
  print(teen)

# We can also use functions instead of SQL queries:
# schemaPeople.groupBy("age").count().orderBy("age").show()

spark.stop()
