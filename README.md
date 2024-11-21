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
# Installation 
# 1. Clone the Repository
git clone https://github.com/yourusername/personal-finance-dashboard.git
cd personal-finance-dashboard

# 2. Install Dependencies
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

# Then, install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
Create a requirements.txt file with the following contents:

txt
Copy code
streamlit
pandas
mysql-connector-python
plotly
# 3. Set Up Database Connection
Update the MySQL connection details in app.py:

python
Copy code

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",  # Change if using a remote MySQL server
        user="your_username",  # Your MySQL username
        password="your_password",  # Your MySQL password
        database="personal_finance"
    )
    return connection
# Usage
1. Run the Streamlit App
After setting up the environment and database, run the app with Streamlit:

streamlit run app.py
# Visualizations
Monthly Spending Trends: Displays a line chart of total spending per month.
Spending by Category: Displays a bar chart showing the total amount spent in each category.
# Acknowledgements
Streamlit for providing an easy-to-use framework for building web apps.
Plotly for interactive data visualizations.
MySQL for database management.
markdown
Copy code

# MySQL Setup

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

