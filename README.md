# Azure Data Engineering Project - Adventure Works Analytics

## 🎯 Project Overview

This end-to-end Azure Data Engineering project demonstrates a complete **Medallion Architecture** implementation using Adventure Works dataset. The project showcases real world data engineering scenarios including API integration, dynamic pipeline creation, and advanced data transformations.

**🔗 [Project Demo Video]([Insert Video Link Here])**

![Project Architecture](images/architecture-diagram.png)

## 🏗️ Architecture

This project implements a **Bronze → Silver → Gold** medallion architecture pattern:

- **Bronze Layer (Raw)**: Ingested data from GitHub API without transformations
- **Silver Layer (Transformed)**: Cleaned and transformed data with business logic
- **Gold Layer (Serving)**: Analytics-ready data warehouse for consumption

![Data Flow](images/data-flow-diagram.png)

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Orchestration** | Azure Data Factory | ETL/ELT pipeline orchestration |
| **Data Processing** | Azure Databricks (PySpark) | Big data transformations |
| **Data Storage** | Azure Data Lake Gen2 | Scalable data lake storage |
| **Data Warehouse** | Azure Synapse Analytics | Serverless SQL analytics |
| **Visualization** | Power BI | Business intelligence dashboards |
| **Security** | Service Principal & Managed Identity | Secure authentication |

## 📊 Dataset

**Adventure Works Sales Dataset** - A comprehensive business dataset containing:
- 📅 3 years of sales data (2015-2017)
- 🛍️ Products, categories, and subcategories
- 👥 Customer demographics and territories  
- 📦 Returns and order information
- 🗓️ Calendar dimension data

![Dataset Overview](images/dataset-overview.png)

## 🚀 Key Features

### ✨ Real-World Scenarios Implemented

- **Dynamic Pipeline Creation**: Parameter-driven pipelines using For-Each loops
- **API Data Ingestion**: Direct data extraction from GitHub repository
- **Advanced PySpark Transformations**: Date functions, string manipulations, aggregations
- **External Table Creation**: Three-step external table setup in Synapse
- **End-to-End Security**: Service Principal and Managed Identity implementation

![Dynamic Pipeline](images/dynamic-pipeline.png)

### 🔧 Advanced Transformations

```python
# Date transformations
df_cal = df_cal.withColumn('Month', month(col('Date')))
df_cal = df_cal.withColumn('Year', year(col('Date')))

# String manipulations  
df_cus.withColumn('FullName', concat_ws(' ', col('Prefix'), col('FirstName'), col('LastName')))

# Data aggregations
df_sales.groupBy('OrderDate').agg(count('OrderNumber').alias('TotalOrders'))
```

![Data Transformations](images/transformations-code.png)

## 🏛️ Project Structure

```
azure-data-engineering-project/
├── 📁 data-factory/
│   ├── pipelines/
│   │   ├── main-pipeline.json
│   │   └── dynamic-pipeline.json
│   ├── datasets/
│   │   ├── ds_http.json
│   │   └── ds_raw.json
│   └── linkedservices/
├── 📁 databricks/
│   ├── notebooks/
│   │   ├── bronze-to-silver.py
│   │   └── data-transformations.py
│   └── configs/
│       └── storage-config.py
├── 📁 synapse/
│   ├── sql-scripts/
│   │   ├── create-external-tables.sql
│   │   ├── create-views.sql
│   │   └── setup-credentials.sql
│   └── schemas/
├── 📁 powerbi/
│   └── adventure-works-dashboard.pbix
├── 📁 configs/
│   └── pipeline-config.json
└── 📁 images/
    └── [Architecture diagrams and screenshots]
```

## ⚙️ Azure Resources Created

| Resource | Name | Purpose |
|----------|------|---------|
| **Resource Group** | `AdventureWorksProject` | Container for all resources |
| **Storage Account** | `adevnturestorage` | Data Lake Gen2 storage |
| **Data Factory** | `adf-adventure-works-project` | ETL orchestration |
| **Databricks** | `adb-aw-project` | Data processing workspace |
| **Synapse Analytics** | `synapse-aw-project` | Data warehouse |
| **App Registration** | `awproject_app` | Service Principal for security |

![Azure Resources](images/azure-resources.png)

## 🔐 Security Implementation

### Service Principal Setup
```python
# Databricks storage access configuration
spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.<storage-account>.dfs.core.windows.net", 
               "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.<storage-account>.dfs.core.windows.net", 
               "<application-id>")
spark.conf.set("fs.azure.account.oauth2.client.secret.<storage-account>.dfs.core.windows.net", 
               "<client-secret>")
```

![Security Setup](images/security-setup.png)

## 📈 Data Pipeline Flow

### Phase 1: Data Ingestion (Bronze Layer)
![Bronze Layer](images/bronze-layer-ingestion.png)

**Dynamic Pipeline Implementation:**
- JSON configuration-driven data ingestion
- For-Each loop for multiple file processing
- HTTP source to Data Lake sink mapping

### Phase 2: Data Transformation (Silver Layer)  
![Silver Layer](images/silver-layer-transformation.png)

**PySpark Transformations:**
- Date dimension creation
- Customer name standardization
- Product SKU cleansing
- Sales metrics calculation

### Phase 3: Data Serving (Gold Layer)
![Gold Layer](images/gold-layer-serving.png)

**Synapse External Tables:**
```sql
-- Create external table in 3 steps
CREATE DATABASE SCOPED CREDENTIAL credential_name
WITH IDENTITY = 'Managed Identity';

CREATE EXTERNAL DATA SOURCE source_name
WITH (LOCATION = 'abfss://silver@storage.dfs.core.windows.net/',
      CREDENTIAL = credential_name);

CREATE EXTERNAL FILE FORMAT parquet_format
WITH (FORMAT_TYPE = PARQUET);
```

## 📊 Analytics & Visualization

![Power BI Dashboard](images/powerbi-dashboard.png)

**Key Metrics Tracked:**
- 📈 Daily sales trends
- 🏆 Top performing products
- 🌍 Regional sales analysis
- 📅 Seasonal patterns
- 🔄 Return analysis

## 🚀 Getting Started

### Prerequisites
- Azure Subscription (Free tier available)
- Power BI Desktop
- Basic knowledge of SQL and Python

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/[your-username]/azure-data-engineering-project.git
   cd azure-data-engineering-project
   ```

2. **Deploy Azure Resources**
   ```bash
   # Create Resource Group
   az group create --name AdventureWorksProject --location eastus
   
   # Deploy resources using ARM template
   az deployment group create --resource-group AdventureWorksProject --template-file deploy/main.json
   ```

3. **Configure Data Factory**
   - Import pipeline definitions from `data-factory/` folder
   - Update connection strings and credentials

4. **Setup Databricks**
   - Import notebooks from `databricks/notebooks/`
   - Configure cluster and storage access

5. **Deploy Synapse Objects**
   - Execute SQL scripts from `synapse/sql-scripts/`
   - Create external tables and views

![Setup Process](images/setup-process.png)

## 💡 Key Learnings & Interview Points

### 🎯 Technical Concepts Mastered

- **Medallion Architecture**: Bronze-Silver-Gold data layering
- **Dynamic Pipelines**: Parameter-driven ADF pipelines
- **PySpark Optimization**: Efficient data transformations
- **External Tables**: Synapse Analytics data virtualization
- **Security Best Practices**: Service Principal implementation

### 🎙️ Interview Questions Covered

1. **"How do you handle dynamic data ingestion?"**
   - Implemented For-Each loops with JSON configuration
   - Parameter-driven pipeline design

2. **"Explain your data transformation approach"**
   - Medallion architecture with clear separation of concerns
   - PySpark transformations with built-in functions

3. **"How do you ensure data security in Azure?"**
   - Service Principal for cross-service authentication
   - Managed Identity for Synapse-Data Lake integration

![Interview Prep](images/interview-points.png)

## 🔧 Troubleshooting Guide

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **Storage Access Denied** | Verify Service Principal permissions |
| **Databricks Cluster Failed** | Check cluster size and region availability |
| **Synapse Query Timeout** | Optimize query with proper filtering |
| **Power BI Connection Error** | Validate SQL endpoint and credentials |

## 📚 Additional Resources

- 📖 [Project Documentation](docs/)
- 🎥 [Video Walkthrough]([Video Link])
- 📝 [Medium Article]([Medium Link])
- 💻 [LinkedIn Post]([LinkedIn Link])

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**[Your Name]**
- 📧 Email: [your.email@domain.com]
- 💼 LinkedIn: [Your LinkedIn Profile]
- 🐱 GitHub: [Your GitHub Profile]

---

⭐ **If this project helped you, please give it a star!** ⭐

![Project Success](images/project-success.png)

> *"This project demonstrates end-to-end Azure Data Engineering capabilities from data ingestion to visualization, showcasing real-world scenarios and best practices."*
