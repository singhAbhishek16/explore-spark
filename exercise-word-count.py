from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinimumTemperature")
sc = SparkContext(conf = conf)

data = sc.textFile("./book.txt")
words = data.flatMap(lambda x:x.split())
word_1 = words.map(lambda x: (x,1))
word_count = word_1.reduceByKey(lambda x,y: x+y)

# to sort the list by frequency of occurance
# strategy - flip (word, frequency) to (frequency, word); then use sortByKey()

flip = word_count.map(lambda x: (x[1], x[0]))
sort_by_frequency = flip.sortByKey()
for each_word in sort_by_frequency.collect():
    print(each_word)