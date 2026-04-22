from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinimumTemperature")
sc = SparkContext(conf = conf)

data = sc.textFile("./1800.csv")
print(f'\nrdd as read from file\n:{data.take(10)}')

# TODO: data.collect() poora dera. find a way to read just 10 rows. and find a way to show in tabular format
# rdd.take(10) & for each_row in rdd.take(10): print(each_row)

def drop_unnecessary_columns(line):
    columns = line.split(',')
    station = columns[0]
    type_of_temp = columns[2]
    temp = columns[3]
    return (station, type_of_temp, temp)

rdd1 = data.map(drop_unnecessary_columns)
print(f'\nrdd1 after using map()\n:{rdd1.take(10)}')
# TODO: filter ke andar wala function likhne ka style note me dal lo
rdd2 = rdd1.filter(lambda x: 'TMAX' in x[1])
print(f'\nrdd2 after using filter()\n:{rdd2.take(10)}')
rdd3 = rdd2.map(lambda x: (x[0], x[2]))
print(f'\nrdd3 after using map()\n:{rdd3.take(10)}')
rdd4 = rdd3.reduceByKey(lambda x,y: max(x, y))
print(f'\nrdd4 after using reduceByKey()\n:{rdd4.take(10)}')
# print(rdd4.collect())
