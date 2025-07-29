CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Hasgot2025729123456789'

-----------------------------------------------------------
-- Create credential 
-----------------------------------------------------------
CREATE DATABASE SCOPED CREDENTIAL cred_awp
WITH
    IDENTITY = 'Managed Identity'



-----------------------------------------------------------
-- External data source to read data from silver container
-----------------------------------------------------------
CREATE EXTERNAL DATA SOURCE source_silver
WITH
(
    LOCATION = 'https://adevnturestorage.dfs.core.windows.net/silver',
    CREDENTIAL = cred_awp
)


-----------------------------------------------------------
-- External data source to write data to gold container
-----------------------------------------------------------
CREATE EXTERNAL DATA SOURCE source_gold
WITH
(
    LOCATION = 'https://adevnturestorage.dfs.core.windows.net/gold',
    CREDENTIAL = cred_awp
)



-----------------------------------------------------------
-- External file format
-----------------------------------------------------------
CREATE EXTERNAL FILE FORMAT format_parquet
WITH
(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)


-----------------------------------------------------------
-- Create external table
-----------------------------------------------------------
CREATE EXTERNAL TABLE gold_extsales
WITH
(
    LOCATION = 'extsales',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = format_parquet
)
AS
SELECT * FROM gold.sales
SELECT * FROM gold_extsales


















