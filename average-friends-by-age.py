# import pandas as pd
#
# data = pd.read_csv("fakefriends.csv", header=None, names=["s.no", "name", "age", "number_of_friends"])
#
# # Q. what is avg number of friends by age?
#
# result = data.groupby("age")["number_of_friends"].mean()
# print(result) # gives expected answer

'''
spark approach
'''

from pyspark import SparkConf, SparkContext
#
conf = SparkConf().setMaster("local").setAppName("AverageFriends")
sc = SparkContext(conf = conf)
#
data = sc.textFile("fakefriends_sample.csv")


print("raw data:\n")
# print(type(data)) # rdd
# print("#######################\n")
print(data.collect())
print("\n")

def drop_unnecessary_columns(line):
    splitted_line = line.split(",")
    age = int(splitted_line[2])
    number_of_friends = int(splitted_line[3])
    return (age, number_of_friends)

rdd2 = data.map(drop_unnecessary_columns)

print("after using map():\n")
print(rdd2.collect())
print("\n")

rdd3 = rdd2.mapValues(lambda x: (x,1))

print("after using mapValues()\n")
print(rdd3.collect())
print("\n")

rdd4 = rdd3.reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1]))
# ('26', ('228184282381145345293298492269254738312439184', 17)) <- additionally 17 ka tracker rakhre spark approach me

print("after using reduceByKeys()\n")
print(rdd4.collect())
print("\n")

rdd5 = rdd4.mapValues(lambda x: x[0]/x[1])

print("after using mapValues()\n")
print(rdd5.collect())
print("\n")