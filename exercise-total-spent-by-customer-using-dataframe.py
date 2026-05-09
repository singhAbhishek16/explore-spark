from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql import functions as func

spark = SparkSession.builder.appName("customerspend").getOrCreate()
schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("item_id", StringType(), True),
    StructField("amount_spent", FloatType(), True)
])

data = spark.read.csv("customer-orders.csv", schema=schema)
filtered_df = data.select("customer_id", "amount_spent")
required_df = filtered_df.groupBy("customer_id").agg(func.round(func.sum("amount_spent"), 2).alias("total_spent"))
# agg(func.round(func.sum("amount_spent"), 2)).alias("total_spent")

sorted_df = required_df.sort("total_spent")

#TODO total_spent wale column ko round karna aur alias kaise use karna - iske notes banalo
'''
required_df = filtered_df.groupBy("customer_id").sum("amount_spent")
sorted_df = required_df.sort("sum(amount_spent)") <-- ek to iss tareke se groupby->sum->sort kar sakte hai

better way,
               func.sum("amount_spent") <------------------------------ step 1: sum
    func.round(func.sum("amount_spent"), 2) <-------------------------- step 2: round
agg(func.round(func.sum("amount_spent"), 2).alias("total_spent")) <---- step 3: alias
filtered_df.groupBy("customer_id").agg(func.round(func.sum("amount_spent"), 2).alias("total_spent"))
'''

result = sorted_df.collect()
for each_item in result:
    print(each_item)

spark.stop()