from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("ExerciseMapValues")
sc = SparkContext(conf = conf)
data = [("alice", 45), ("bob", 65), ("charlie", 32), ("diana", 91)]
grades_rdd = sc.parallelize(data)

def result(x):
    if x>50:
        return "pass"
    else:
        return "fail"

results = grades_rdd.mapValues(result) # mapValues() me ek function pass hota hai, jiska input rdd ke values hote hai. ek ek karke wo values pass hote hai
print(results.collect())