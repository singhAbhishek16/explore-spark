from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TotalSpentByCustomer")
sc = SparkContext(conf = conf)

data = sc.textFile("customer-orders.csv")

def remove_unnecessary_lines(line):
    each_value = line.split(",")
    customer_id = each_value[0]
    amount_spent = float(each_value[2])
    return (customer_id, amount_spent)

cleaned_data = data.map(remove_unnecessary_lines)
total_amount_spent = cleaned_data.reduceByKey(lambda x,y: (x+y))
sorted_total_amount = total_amount_spent.map(lambda x: (x[1], x[0])).sortByKey()

for each_item in sorted_total_amount.collect():
    print(each_item)