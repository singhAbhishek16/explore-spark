data = {
    "name": ["will", "jean", "hugh","deanna","quark"],
    "age": [33,33,55,40,68],
    "friends": [385,2,221,465,21],
}

# find average number of friends by age

# pandas approach
import  pandas as pd
df=pd.DataFrame(data)
avg_friends_by_age=df.groupby("age")["friends"].mean()
print(avg_friends_by_age)

# spark approach


