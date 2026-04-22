from pyspark import SparkConf, SparkContext
import time
import tracemalloc

start = time.time()
tracemalloc.start()

conf = SparkConf().setMaster("local").setAppName("AverageFriends")
sc = SparkContext(conf = conf)

data = sc.textFile("upi_10m.csv")

# <- answers total transaction amount by city
def remove_unnecessary_columns(line):
    each_value = line.split(',')
    city = each_value[2]
    amount = float(each_value[5])
    return (city, amount)

cleaned_data = data.map(remove_unnecessary_columns)
amount_by_city = cleaned_data.reduceByKey(lambda x,y: x+y)
print(amount_by_city.collect()) # <- answers total transaction amount by city

# def filter_failure_transactions(line):
#     each_value = line.split(',')
#     city = each_value[2]
#     transaction_status = each_value[7]
#     if transaction_status == "FAILED":
#         return (city, transaction_status)
#     else:
#         return (None, None)
# #
# map_transaction_type = data.map(filter_failure_transactions)
# failed_transactions = map_transaction_type.filter(lambda x: x[0] is not None)
# count_failed_transactions = failed_transactions.mapValues(lambda x: (x,1))
# count_failed_transactions_with_cities = count_failed_transactions.reduceByKey(lambda x,y: x+y)
# print(count_failed_transactions_with_cities.collect())

end = time.time()
print(f"Time taken by spark: {end - start:.2f} seconds")
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Peak memory in spark: {peak / 1024 / 1024:.2f} MB")

