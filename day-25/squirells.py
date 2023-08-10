import pandas

data = pandas.read_csv("squirrel_data.csv")
print(data.dtypes)


print(  data["Primary Fur Color"].unique()  )



count = data["Primary Fur Color"].value_counts()
print(count)
count.to_csv("squirrel_count.csv")









