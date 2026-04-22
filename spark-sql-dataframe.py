from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true").csv("fakefriends-header.csv")

people.groupBy("age").mean("friends").orderBy("age").show()

# # print(f'type(people): {type(people)}') # <class 'pyspark.sql.classic.dataframe.DataFrame'>
#
# # print("Here is our inferred schema:")
# # people.printSchema()
#
# # print("Let's display the name column:")
# # people.select("name").show()
# # #
# # print("Filter out anyone over 21:")
# # people.filter(people.age < 21).show()
# # #
# # print("Group by age")
# # people.groupBy("age").mean("friends").show()
# # #
# # print("Make everyone 10 years older:")
# # people.select(people.name, people.age + 10).show()
#
# # show one column
# people.select(people.name).show()
#
# # show multiple columns
# people.select(people.name, people.age).show()
#
# # to get gist (top 20 rows) of table
# people.show()
#
# # row pe filter laga kar
# people.filter(people.age<18).show()
#
# # nusing groupBy
# people.groupBy("age").mean("friends").show()
#
# # row count
# print(people.count())
#
# # column count
# print(len(people.columns))



















spark.stop()

