Here’s a sample `README.md` file for the solutions provided to the questions:

---

# **Data Manipulation Solutions**

This project contains Python solutions to a set of data manipulation tasks, including:
1. Aggregating weather data while handling missing fields.
2. Performing prime factorization of a given integer.
3. SQL query to update product prices by 10% and display the results.

## **Table of Contents**
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Details of Each Solution](#details-of-each-solution)
    - [Weather Data Aggregation](#1-weather-data-aggregation)
    - [Prime Factorization](#2-prime-factorization)
    - [SQL Query to Update Prices](#3-sql-query-to-update-prices)
- [Contact](#contact)

---

## **Project Overview**
This project provides solutions to common data manipulation tasks:
1. **Weather Data Aggregation**: Aggregates weather data such as temperature and humidity, gracefully handling missing data.
2. **Prime Factorization**: Computes the prime factorization of any given integer and returns prime factors with their respective exponents.
3. **SQL Query**: A SQL query that increases the price of all products by 10% and displays the new price along with the product name.

---

## **Requirements**
- Python 3.x installed on your system.

---

## **Installation and Setup**
1. Clone or download the repository containing this project.
2. Navigate to the project folder (`data_manipulation_solution`).

---

## **Usage**
1. To run the Python code for weather data aggregation and prime factorization:
   - Open a terminal/command prompt in the `data_manipulation_solution` folder.
   - Execute the following command:
     ```bash
     python solution.py
     ```
   This will run the Python script and display the results for both tasks.

2. The SQL query can be executed directly on a database management system where a table named `products` exists. It will update the prices and display the results.

---

## **Details of Each Solution**

### **1. Weather Data Aggregation**

This Python function processes a list of dictionaries where each dictionary represents a record of weather data (city name, temperature, and humidity). It aggregates the data by city and calculates the average temperature and humidity, handling missing values gracefully.

#### Example:
```python
records = [
    {'city': 'New York', 'temperature': 22, 'humidity': 60},
    {'city': 'Los Angeles', 'temperature': 28},
    {'city': 'New York', 'humidity': 65},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 40},
    {'city': 'Chicago', 'temperature': 15, 'humidity': 55}
]
```

#### Expected Output:
```
{
    'New York': {'average_temperature': 22.0, 'average_humidity': 62.5},
    'Los Angeles': {'average_temperature': 29.0, 'average_humidity': 40.0},
    'Chicago': {'average_temperature': 15.0, 'average_humidity': 55.0}
}
```

---

### **2. Prime Factorization**

The function takes an integer input and returns a list of tuples, where each tuple contains a prime factor of the number and its exponent.

#### Example:
```python
n = 60
```

#### Expected Output:
```
[(2, 2), (3, 1), (5, 1)]
```

---

### **3. SQL Query to Update Prices**

This SQL query increases the price of all products by 10% and displays the new price along with the product name:

```sql
SELECT
    name,
    price * 1.10 AS new_price
FROM
    products;
```

This query calculates the updated price for each product without altering the original data in the database. It is intended for use on any relational database containing a `products` table with columns `name` and `price`.

---

## **Contact**
For any queries or assistance, please contact me at:
- **Email**: [polepallynithishreddy@gmail.com](mailto:polepallynithishreddy@gmail.com)

---

This `README.md` provides instructions on how to set up and run the Python scripts as well as how to use the SQL query in your database system.
