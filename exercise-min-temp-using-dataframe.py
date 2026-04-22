# 1. sabse pehle csv read karna hai, prerequisite kya hai?
# 0. spark ka session banao. aur csv me header nhi hai to mere script me schema define karo

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("mintemp").getOrCreate()
schema = StructType([
    StructField("stationid", StringType(), True),
    StructField("date", IntegerType(), True),
    StructField("measure_type", StringType(), True),
    StructField("temperature", FloatType(), True)

])
df = spark.read.schema(schema).csv("1800.csv")

'''
yaha tak boiler plate code ho gaya. also upar schema define kiya hai wo jaisi meri csv hai, uske according tied nhi hai
csv me 7 columns hai, last 3 empty hai. to StructType me 4 column define karenge to baki csv ke bas 4 column he read karega
agar 7 define kiye StructType me to 7 columns read kiya
agar 8 define kiye StructType me to 8 column banaya (last column NULL)
+-----------+--------+------------+-----------+----+----+----+----+----+
|  stationid|    date|measure_type|temperature|col1|col2|col3|col4|col5|
+-----------+--------+------------+-----------+----+----+----+----+----+
|ITE00100554|18000101|        TMAX|      -75.0|NULL|NULL|   E|NULL|NULL|
'''

# 2. TMAX wale saaare rows drop kardo
# 3. date, measure_type columns drop kardo
# 4. stationid se groupBy; min(temperature)

filtered_df = df.filter(df.measure_type=="TMIN")
selected_df = filtered_df.select("stationid", "temperature")
required_df = selected_df.groupBy("stationid").min("temperature")

'''
upar har step me ek naya df bana hai; wohi wala update nhi hua hai. filtered_df abhi print karoge to same state me hai
ie filtered_df != required_df
'''

'''
section-1: boilerplate
section-2: logic
section-3: showing result in better format
'''

results = required_df.collect()
for result in results:
    print(result)

spark.stop()