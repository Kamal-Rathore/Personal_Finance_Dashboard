import pandas as pd
import streamlit as st
import plotly.express as px
import mysql.connector
from mysql.connector import Error

# MySQL connection setup
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="123456",  # Replace with your MySQL password
            database="personal_finance"
        )
        return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Function to upload data to MySQL
def upload_to_db(data):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            for _, row in data.iterrows():
                cursor.execute("""
                    INSERT INTO transactions (date, amount, category)
                    VALUES (%s, %s, %s)
                """, (row['Date'], row['Amount'], row['Category']))
            conn.commit()
            st.success("Data uploaded successfully!")
        except Error as e:
            st.error(f"Failed to upload data: {e}")
        finally:
            cursor.close()
            conn.close()

# Function to fetch data from MySQL
def fetch_from_db():
    conn = connect_to_db()
    if conn:
        query = "SELECT date, amount, category FROM transactions"
        data = pd.read_sql(query, conn)
        conn.close()
        return data
    else:
        return pd.DataFrame()  # Return an empty DataFrame on failure

# Streamlit app
st.title("Personal Finance Dashboard")
st.write("Analyze your spending trends over time and by category.")

# File Upload
uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=['csv'])

if uploaded_file:
    try:
        # Load dataset
        df = pd.read_csv(uploaded_file)

        # Check required columns
        required_columns = ['Date', 'Amount', 'Category']
        if not all(col in df.columns for col in required_columns):
            st.error(f"Missing required columns: {', '.join([col for col in required_columns if col not in df.columns])}")
        else:
            # Data Cleaning
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
            df.dropna(subset=['Date', 'Amount'], inplace=True)

            # Display cleaned data
            st.subheader("Cleaned Data")
            st.dataframe(df.head())

            # Upload data to MySQL
            if st.button("Upload Data to Database"):
                upload_to_db(df)

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Upload a CSV file to proceed.")

# Fetch and display data from MySQL
st.subheader("Data from Database")
data = fetch_from_db()
if not data.empty:
    st.dataframe(data)

    # Monthly Spending Analysis
    data['Date'] = pd.to_datetime(data['date'])
    data['Month_Year'] = data['Date'].dt.to_period('M')
    monthly_spending = data.groupby('Month_Year')['amount'].sum().reset_index()
    monthly_spending['Month_Year'] = monthly_spending['Month_Year'].astype(str)

    # Line Chart using Plotly
    st.subheader("Monthly Spending Trends")
    line_chart = px.line(
        monthly_spending,
        x='Month_Year',
        y='amount',
        markers=True,
        title='Monthly Spending Trends'
    )
    st.plotly_chart(line_chart)

    # Spending by Category
    st.subheader("Spending by Category")
    category_spending = data.groupby('category')['amount'].sum().reset_index()
    category_spending = category_spending.sort_values(by='amount', ascending=False)

    # Bar Chart for Spending by Category
    bar_chart = px.bar(
        category_spending,
        x='amount',
        y='category',
        orientation='h',
        title='Spending by Category',
        color='category',
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(bar_chart)
else:
    st.warning("No data available in the database.")
