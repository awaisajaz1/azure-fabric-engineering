# Azure Fabric Earthquake Data Pipeline

## 📌 Overview
This project implements a **data pipeline** using **Azure Fabric** to process earthquake data from the **US Earthquake API**. The solution follows **Medallion Architecture**, utilizes **Delta Tables**, and provides real-time insights via **Power BI** dashboards.

## 🚀 Architecture
- **Data Source**: US Earthquake API () → Azure Fabric **Lakehouse**
- **Processing**: PySpark Notebooks
- **Storage**: **Delta Tables** (Bronze → Silver → Gold)
- **Orchestration**: Azure Fabric **Data Pipeline**
- **Visualization**: SQL Endpoint for **Power BI Dashboards**

  ## 📖 API Documentation
For more details, visit the [US Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/).
🔹 Open Link in a New Tab (GitHub Flavored Markdown Doesn't Support This)
However, if you’re using HTML within Markdown, you can force the link to open in a new tab:

md
Copy
Edit
<a href="https://earthquake.usgs.gov/fdsnws/event/1/" target="_blank">US Earthquake API</a>
Would you like me to add an external link to your README? 🚀

## 🔹 Features
✅ **Lakehouse Architecture** for scalable data storage  
✅ **Medallion Architecture** for structured data refinement  
✅ **Merge Strategy** for incremental updates  
✅ **Delta Tables** for ACID compliance & fast queries  
✅ **SQL Endpoint** for direct Power BI integration  

## 🛠️ Tech Stack
- **Azure Fabric** (Lakehouse, Data Pipeline, SQL Endpoint)
- **PySpark** for data transformation
- **Delta Lake** for efficient storage
- **Power BI** for visualization

## 📂 Data Processing Flow
1️⃣ **Bronze Layer** → Stores raw earthquake data  
2️⃣ **Silver Layer** → Cleans & transforms data  
3️⃣ **Gold Layer** → Provides aggregated insights  

## 📊 Power BI Dashboard
- 🌎 **Real-time Earthquake Monitoring**
- 📈 **Historical Trends & Analytics**
- 🔍 **Filters for Magnitude, Location, and Time Range**

## ⚙️ Setup & Deployment
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/azure-fabric-earthquake.git
cd azure-fabric-earthquake
