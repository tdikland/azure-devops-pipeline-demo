# Databricks notebook source
# SETUP

# data = [
#   (1, " Mark"),
#   (2, "Lisa "),
#   (3, "Sophie")
# ]
# df_raw = spark.createDataFrame(data, "id INT, value STRING")
# df_raw.display()

# df_raw.write.mode("overwrite").saveAsTable("tim_dikland.sse.example_data")

# COMMAND ----------

from src.transform import cleanse_name_column

df_raw = spark.read.table("tim_dikland.sse.example_data")
df_clean = df_raw.transform(cleanse_name_column)
df_clean.display()

# COMMAND ----------

df_clean.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("tim_dikland.sse.example_data_cleansed")

# COMMAND ----------


