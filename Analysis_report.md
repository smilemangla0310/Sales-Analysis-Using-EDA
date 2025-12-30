### **📊 Sales Data Analysis Report**



##### 1\. Introduction

This report presents a detailed analysis of the sales dataset provided for the assignment.

The objective is to:

* Explore the dataset
* Clean the data
* Analyze product performance
* Calculate total revenue
* Identify top-performing items and regions
* Provide business insights
* 

All analysis was performed using Python, Pandas, and Jupyter Notebook.



##### **2. Dataset Overview**

**Columns Included**



* Date
* Product
* Quantity
* Price
* Customer\_ID
* Region
* Total\_Sales (Quantity × Price)



**Basic Information**

* Total Rows: 100
* Total Columns: 7
* No missing values found
* No duplicate rows found



**Data types:**

**int64 → Quantity, Price, Total\_Sales**

**object → Date, Product, Customer\_ID, Region**



##### **3. Data Cleaning Steps**

* to check for the null values:

           **df.isnull().sum()**

**Result:**

**➡ No missing values**



* Duplicate Rows



**Checked using:**

**df.duplicated().sum()**



**Result:**

**➡ 0 duplicates**



The dataset was clean and ready for analysis.



#####  **4. Exploratory Data Analysis (EDA)**

Product Count

**df\['Product'].value\_counts()**



**| Product    | Count |**

**| Tablet     | 26    |**

**| Laptop     | 24    |**

**| Phone      | 20    |**

**| Headphones | 15    |**

**| Monitor    | 15    |**





**Most sold product:** *Tablet*



##### <b> 5. Revenue Analysis</b>

Total Revenue:

**df\['Revenue'].sum()**



**Total Revenue Generated: ₹12365048**



Revenue by Product:

**df.groupby('Product')\['Revenue'].sum()**



This identifies which products contribute the most to total revenue.



**Highest revenue-generating product: Laptop**



Revenue by Region:

**df.groupby('Region')\['Revenue'].sum()**



##### **6. Key Insights \& Findings**



1\. Most Sold Product**:**

**Tablet**

(Tablet had the highest number of transactions.)



2\. Highest Revenue Product:

**Laptop**

(Even though it sold slightly less, its price generated high revenue.)



3\. Strong Revenue Regions:

 **North Region is the highest Revenue Region.**

                                 

4\. No missing or duplicate data

**Dataset was perfectly clean.**



**5. Business Recommendation**



* Promote Laptop through ads — it brings maximum revenue.
* Increase stock for Tablet as it sells the most.
* Focus more marketing on top-performing regions.



**7. Conclusion**



The sales analysis shows clear trends in product performance and revenue distribution.

Laptop is the top revenue generator, while Tablet is the highest-selling product.

These insights can guide marketing strategies, inventory decisions, and business planning.



**8. Files Included**



sales\_analysis.py – Full analysis code

sales\_data.csv – Original dataset

analysis\_report.md – This report

requirements.txt – Required libraries







