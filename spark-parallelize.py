from pyspark import SparkConf, SparkContext

'''
spark boilerplate dala pehle - 1. configuration; 2. spark context
'''
conf = SparkConf().setMaster("local").setAppName("SparkBoilerplate")
sc = SparkContext(conf = conf)

'''
parallelize() kya karta hai? python collection (list/tuple/..) input leta hai aur rdd bana deta hai
rdd banane ke addition me wo multiple partitions me distribute bhi kar deta hai.
example here: [1,2,3,4,5] ko 3 partition me daal diya - [1,2] [3,4] [5]
-> parallelize is only used jab mera data chhota ho, code me he ho. agar external(big) file se uthani hoto, we never use
'''

# data = [1,2,3,4,5]
# rdd = sc.parallelize(data)

# data = {
#     "abhishek": 1,
#     "sbhubham": 2,
#     "xyz": 3
# }
# rdd = sc.parallelize(data.items())

'''
for list, tuple - sc.parallelize(data)
for dict - sc.parallelize(data.items())
'''

# print(rdd)
# print(rdd.collect())


# grades = sc.parallelize([
#     ("alice", 45),
#     ("bob", 72),
#     ("charlie", 38),
#     ("diana", 91)
# ])
# result = grades.mapValues(lambda x: True if x>50 else False)
# print(result.collect())

'''
mapValues kya karta hai? - 
sabse pehle, rdd ka input dict hona chahiye.
uske baad, mapValues bas dict ke values me update karta hai, leaves keys untouched
'''

sales = sc.parallelize([
    ("north", 200),
    ("south", 150),
    ("north", 300),
    ("south", 250),
    ("north", 100),
])

result = sales.reduceByKey(lambda x,y: (x+y)/2)
print(result.collect())


