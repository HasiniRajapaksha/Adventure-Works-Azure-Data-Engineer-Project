CREATE VIEW gold.calender
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK ' /AdventureWorks_Calendar/',
        FORMAT = 'PARQUET'
    ) as QUERY1

    
CREATE VIEW gold.customers
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK 'https://adevnturestorage.dfs.core.windows.net/silver/AdventureWorks_Customers/',
        FORMAT = 'PARQUET'
    ) as QUERY1


CREATE VIEW gold.products
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK 'https://adevnturestorage.dfs.core.windows.net/silver/AdventureWorks_Products/',
        FORMAT = 'PARQUET'
    ) as QUERY1


CREATE VIEW gold.ret
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK 'https://adevnturestorage.dfs.core.windows.net/silver/AdventureWorks_Returns/',
        FORMAT = 'PARQUET'
    ) as QUERY1


CREATE VIEW gold.sales
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK 'https://adevnturestorage.dfs.core.windows.net/silver/AdventureWorks_Sales/',
        FORMAT = 'PARQUET'
    ) as QUERY1

CREATE VIEW gold.territories
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK 'https://adevnturestorage.dfs.core.windows.net/silver/AdventureWorks_Territories/',
        FORMAT = 'PARQUET'
    ) as QUERY1


CREATE VIEW gold.subcategories
AS
SELECT
      *
FROM
    OPENROWSET(
        BULK 'https://adevnturestorage.dfs.core.windows.net/silver/Product_Subcategories/',
        FORMAT = 'PARQUET'
    ) as QUERY1












