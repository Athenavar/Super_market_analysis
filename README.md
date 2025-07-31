# Supermarket Sales Analysis

## Project Overview
This project presents an interactive data analysis dashboard built using Python and Streamlit, designed to visualize and explore sales data from a supermarket. The application provides insights into various sales metrics and customer behaviour through meaningful visualizations.

## Objective
The primary goal is to analyse supermarket sales data and extract valuable insights using data visualization tools. The
dashboard allows users to: - Upload a CSV dataset
- View key summary statistics
- Analyse gender-wise and weekday vs. weekend sales
- Explore product line performance
- Understand commonly used payment methods

## Dataset Information
- **Source**: Supermarket Sales Dataset (Kaggle)
- **File Format**: CSV
- **Records**: 1000 rows
- **Fields**: 17 columns

### Key Columns:
- Invoice ID, Branch, City
- Customer Type, Gender
- Product Line, Unit Price, Quantity
- Total, Date, Time, Payment

## Google Colab Notebook
You can explore the EDA and visualizations using the Colab notebook here:
[Open in Google Colab] (https://colab.research.google.com/drive/1Kj9zsvoZ-Nlo5ZwBtkBzreJB8JkHQgVh#)

## Tools and Technologies Used

Technology     Purpose
Python         Core programming language
Pandas         Data manipulation and preprocessing
Matplotlib     Static data visualization
Seaborn        Statistical visualization
Steamlit       Web application/dashboard framework
Google Colab   Initial data exploration

## Dashboard Features
- File upload option for CSV input
- Interactive visualizations for gender distribution
- Analysis of product line performance
- Weekday versus weekend sales comparison
- Overview of preferred payment methods
- Simple and intuitive interface

## How to Run the Application
### Prerequisites:
Ensure Python is installed. Then install the required libraries using:

pip install streamlit pandas matplotlib seaborn

Run the Dashboard
In your command prompt or terminal, navigate to the project directory and run:
Python -m streamlit run supermarket_dashboard.py
After running the above command, your browser will automatically open the dashboard at:
http://localhost:8501

Once open, upload the supermarket_sales.csv file when prompted. 
