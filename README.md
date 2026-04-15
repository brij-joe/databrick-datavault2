# Data Vault 2.0 Implementation on Databricks

## 📌 Overview

This repository contains a sample **Databricks notebook** demonstrating how to implement the **Data Vault 2.0 modeling approach** using modern data engineering practices.

The solution follows a **Medallion Architecture** pattern:

* **Bronze Layer** → Raw source-aligned schema
* **Silver Layer** → Data Vault 2.0 model
* **Gold Layer** → Kimball's dimensional model (Data Mart)

This layered approach ensures scalability, auditability, and optimized analytics consumption.

---

## 🏗️ Architecture

### 🔶 Bronze Layer (Raw / Source-Aligned)

* Stores raw ingested data in its original structure
* Minimal transformations applied
* Acts as a single source of truth for ingestion

### ⚪ Silver Layer (Data Vault 2.0)

Implements Data Vault 2.0 modeling:

#### Hubs

* Store unique business keys
* Example: Customer ID, Order ID

#### Links

* Represent relationships between hubs
* Example: Customer ↔ Order

#### Satellites

* Store descriptive attributes and history
* Example: Customer details, Order status

---

### 🟡 Gold Layer (Data Mart - Kimball Model)

* Built using **Kimball Dimensional Modeling**
* Optimized for reporting and analytics
* Includes:

  * **Fact tables** (transactions, measures)
  * **Dimension tables** (Customer, Date, Product)

---

## ⚙️ Technologies Used

* **Databricks Notebook**
* **PySpark**
* **Delta Lake**
* **SQL**

---

## 📂 Project Structure

```
.
├── notebooks/
│   └── customer_order.ipynb
├── data/
│   └── sample datasets
├── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Databricks workspace
* Basic knowledge of PySpark and SQL
* Access to sample data (included or external)

### Steps to Run

1. Import the notebook into Databricks:

   * Go to Workspace → Import → Upload `.ipynb`

2. Attach a cluster:

   * Use a runtime with Spark + Delta support

3. Run the notebook:

   * Execute cells sequentially

---

## 🔄 End-to-End Workflow

1. **Ingest Raw Data into Bronze Layer**
2. **Apply Data Vault Modeling in Silver Layer**

   * Generate Business Keys
   * Load Hubs
   * Create Links
   * Populate Satellites
3. **Transform into Gold Layer (Dimensional Model)**

   * Build Fact Tables
   * Build Dimension Tables
4. **Enable Analytics & Reporting**

---

## 💡 Key Features

* End-to-end **Medallion Architecture implementation**
* Data Vault 2.0 modeling in Silver layer
* Kimball dimensional modeling in Gold layer
* Incremental data loading
* Historical tracking (SCD Type 2)
* Clear separation of ingestion, modeling, and consumption layers
* Optimized for cloud-scale analytics

---

## 📊 Example Use Case

This notebook demonstrates:

* Customer and Order data ingestion
* Relationship modeling using Data Vault
* Transformation into analytics-ready dimensional model
* Historical tracking of changes across layers

---

## 🧠 Why This Approach?

### Data Vault 2.0 (Silver)

* Scalable and flexible modeling
* Full auditability and lineage
* Handles schema evolution efficiently

### Kimball's Dimesnsional Models (Gold)

* High-performance analytics
* Business-friendly schema
* Optimized for BI tools

### Medallion Architecture

* Clear separation of concerns
* Improved data quality across layers
* Supports both raw and curated data needs

---

## 🔮 Future Enhancements

* Metadata-driven pipeline automation
* Integration with orchestration tools (e.g., Airflow)
* Streaming ingestion support
* Data quality and validation framework
* CI/CD for data pipelines

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests for improvements.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👤 Author

**Brijesh Singh**

---

## ⭐ Support

If you found this useful, please consider giving it a star ⭐ on GitHub!

---
