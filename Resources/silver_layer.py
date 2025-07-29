# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC # SILVER LAYER SCRIPT

# COMMAND ----------

# MAGIC %md
# MAGIC ### DATA ACESS USING APP

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.adevnturestorage.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.adevnturestorage.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.adevnturestorage.dfs.core.windows.net", "63371958-580d-40e9-882e-6aeacb96190e")
spark.conf.set("fs.azure.account.oauth2.client.secret.adevnturestorage.dfs.core.windows.net", "FPm8Q~mbZrxe4NOkWzF9fwMreaG~xWv2k760wb2j")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.adevnturestorage.dfs.core.windows.net", "https://login.microsoftonline.com/aa232db2-7a78-4414-a529-33db9124cba7/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC ### DATA LOADING

# COMMAND ----------

# MAGIC %md
# MAGIC #### Read Data from Dataset that store in Azure Data Lake Storage

# COMMAND ----------

df_cal = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Calendar')

# COMMAND ----------

df_cus = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Customers')

# COMMAND ----------

df_procat = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Product_Categories')

# COMMAND ----------

df_pro = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Products')

# COMMAND ----------

df_ret = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Returns')

# COMMAND ----------

df_sales = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_ter = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/AdventureWorks_Territories')

# COMMAND ----------

df_subcat = spark.read.format('csv')\
    .option("header",True)\
    .option("InferSchema",True)\
    .load('abfss://bronze@adevnturestorage.dfs.core.windows.net/Product_Subcategories')

# COMMAND ----------

# MAGIC %md
# MAGIC ### TRANSFORMATION

# COMMAND ----------

# MAGIC %md
# MAGIC #### calendar

# COMMAND ----------

df_cal = df_cal.withColumn('Month', month(col('Date')))\
               .withColumn('Year',year(col('Date')))
df_cal.display()


# COMMAND ----------

df_cal.write.format('parquet')\
             .mode('append')\
             .option("path","abfss://silver@adevnturestorage.dfs.core.windows.net/AdventureWorks_Calendar")\
             .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### customer

# COMMAND ----------

df_cus.display()

# COMMAND ----------

# one way to contact columns
df_cus.withColumn("fullname",concat(col('Prefix'), lit(' '), col('FirstName'), lit(' '), col('lastName')))

#second way 
df_cus.withColumn('fullName',concat_ws(' ', col('Prefix'), col('FirstName'), col('lastName'))).display()

# COMMAND ----------

df_cus.write.format('parquet')\
            .mode('append')\
            .option('path','abfss://silver@adevnturestorage.dfs.core.windows.net/AdventureWorks_Customers')\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sub Category

# COMMAND ----------

df_subcat.display()

# COMMAND ----------

df_subcat.write.format('parquet')\
         .mode('append')\
         .option('path','abfss://silver@adevnturestorage.dfs.core.windows.net/Product_Subcategories')\
         .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Product

# COMMAND ----------

df_pro.display()

# COMMAND ----------

df_pro = df_pro.withColumn('ProductSKU',split(col('ProductSKU'),'-')[0])\
       .withColumn('ProductName',split(col('ProductName'),'-')[0])

# COMMAND ----------

df_pro.display()

# COMMAND ----------

df_pro.write.format('parquet')\
             .mode('append')\
             .option("path","abfss://silver@adevnturestorage.dfs.core.windows.net/AdventureWorks_Products")\
             .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Returns

# COMMAND ----------

df_ret.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@adevnturestorage.dfs.core.windows.net/AdventureWorks_Returns")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Territories

# COMMAND ----------

df_ter.display()

# COMMAND ----------

df_ret.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@adevnturestorage.dfs.core.windows.net/AdventureWorks_Territories")\
            .save()


# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales = df_sales.withColumn('StockDate',to_timestamp('StockDate'))
df_sales = df_sales.withColumn('OrderNumber',regexp_replace(col('OrderNumber'),'S','T'))
df_sales = df_sales.withColumn('Multiply',col('OrderLineItem')*col('OrderQuantity'))

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.groupBy('OrderDate').agg(count('OrderNumber')).alias('TotalOrder').display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Product Category

# COMMAND ----------

df_procat.display()

# COMMAND ----------

df_sales.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@adevnturestorage.dfs.core.windows.net/AdventureWorks_Sales")\
            .save()