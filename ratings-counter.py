from pyspark import SparkConf, SparkContext
'''
SparkConf → used to configure your Spark app (like settings)
SparkContext → the entry point to Spark itself — the thing that actually starts Spark and lets you talk to it
Think of SparkConf as a settings form and SparkContext as the ignition key that starts the Spark engine.
'''
import collections
import inspect

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("/Users/abhishek/explore-spark/ml-100k/u.data")
print(f'type(lines): {type(lines)} \n') # <class 'pyspark.core.rdd.RDD'>
print(f'type(lines.take()): {type(lines.take(10))} \n') # <class 'list'>
print(f'lines-rdd: {lines.take(10)} \n') # ['196\t242\t3\t881250949', '186\t302\t3\t891717742', '22\t377\t1\t878887116', '244\t51\t2\t880606923', '166\t346\t1\t886397596', '298\t474\t4\t884182806', '115\t265\t2\t881171488', '253\t465\t5\t891628467', '305\t451\t3\t886324817', '6\t86\t3\t883603013']
'''
# sc.textFile() se file read karke RDD bana liya. ye RDD me files ke saare individual lines
# ek dataset me store ho gaye
# spark step: transform
'''
ratings = lines.map(lambda x: x.split()[2])
print(f'inspect.getfile(type(ratings)): {inspect.getfile(type(ratings))}\n') # /opt/homebrew/Cellar/apache-spark/4.1.1/libexec/python/lib/pyspark.zip/pyspark/core/rdd.py
print(f'type(ratings): {type(ratings)} \n') # <class 'pyspark.core.rdd.PipelinedRDD'>
print(f'type(ratings.take()): {type(ratings.take(10))} \n') # <class 'list'>
print(f'ratings-rdd: {ratings.take(10)} \n') # ['3', '3', '1', '2', '1', '4', '2', '5', '3', '3']
'''
# lines wale RDD ko map() me pass karke bas 2nd column ie rating values ko naye RDD me le liya
# spark step: transform'''

result = ratings.countByValue()
print(f'type(result): {type(result)} \n') # <class 'collections.defaultdict'>
'''
# result is no more an RDD now. its normal python.
# spark step: action'''


sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
