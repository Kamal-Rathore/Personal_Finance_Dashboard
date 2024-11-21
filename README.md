# Personal Finance Dashboard

This is a personal finance dashboard built with **Streamlit**, **MySQL**, and **Plotly**. The application allows users to upload their daily transaction data in CSV format, store it in a MySQL database, and visualize their spending trends over time and by category.

## Features
- **CSV File Upload**: Upload a CSV file containing transaction data with `Date`, `Amount`, and `Category` columns.
- **Data Cleaning**: The app cleans the uploaded data and stores it in a MySQL database.
- **Data Visualization**:
  - **Monthly Spending Trends**: Displays a line chart of total spending per month.
  - **Spending by Category**: Shows a bar chart of spending per category.
- **MySQL Integration**: All data is stored in a MySQL database for easy retrieval and analysis.

## Prerequisites

Before running the app, ensure that the following dependencies are installed:

- Python 3.x
- MySQL (running locally or remotely)
- Required Python packages (see below)

### MySQL Setup

1. Install MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/installer/).
2. Create a database and table for storing transaction data:

```sql
CREATE DATABASE personal_finance;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(100) NOT NULL
);

# Installation
# 1. Clone the Repository
