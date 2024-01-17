import pyspark.sql.functions as F

def cleanse_name_column(df):
    return df.withColumn("name", F.trim("value")).select("id", "name")