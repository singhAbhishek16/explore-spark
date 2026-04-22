# Q. Which Indian city had the highest UPI transaction volume in 2023?
# Q. Which Indian city had the highest failure transaction in 2023?

import pandas as pd
import time
import tracemalloc

start = time.time()
tracemalloc.start()

data = pd.read_csv("upi_sample.csv")
total_amount_by_city = data.groupby("city")["amount_inr"].sum()
print("\ntotal amount of UPI transactions by city:")
print(total_amount_by_city)


# print(data[data["status"] == "FAILED"])
# print("\nwhich city faced highest number of failed transactions?")
# failed_data = data[data["status"] == "FAILED"]
# failure_status_by_city = failed_data.groupby("city")["status"].count()
# print(failure_status_by_city)

end = time.time()
print(f"Time taken by pandas: {end - start:.2f} seconds")

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Peak memory in pandas: {peak / 1024 / 1024:.2f} MB")