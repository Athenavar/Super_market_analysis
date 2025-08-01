import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Title
st.title("🛒 Supermarket Sales Analysis Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload the Supermarket Sales CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total Sales'] = df['Quantity'] * df['Unit price']
    df['Day of Week'] = df['Date'].dt.dayofweek
    df["Weekend"] = df["Day of Week"].apply(lambda x: "Weekend" if x >= 5 else "Weekday")

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🧠 Insights", "📈 Trends", "🗃️ More"])

    with tab1:
        st.subheader("📌 Dataset Preview")
        st.dataframe(df.head(10))

        st.subheader("🧮 Summary Statistics")
        st.write(df.describe())

    with tab2:
        st.subheader("Top Product Lines by Sales")
        top_products = df.groupby('Product line')['Total Sales'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots()
        sns.barplot(x=top_products.values, y=top_products.index, palette="viridis", ax=ax)
        ax.set_title("Top Product Lines")
        st.pyplot(fig)

        st.subheader("Sales by Gender")
        gender_sales = df.groupby("Gender")["Total Sales"].sum()
        fig, ax = plt.subplots()
        sns.barplot(x=gender_sales.index, y=gender_sales.values, palette="pastel", ax=ax)
        ax.set_title("Sales by Gender")
        st.pyplot(fig)

    with tab3:
        st.subheader("Monthly Sales Trend")
        df.set_index("Date", inplace=True)
        monthly_sales = df['Total Sales'].resample('M').sum()
        fig, ax = plt.subplots()
        monthly_sales.plot(marker='o', ax=ax)
        ax.set_title("Monthly Sales Trend")
        st.pyplot(fig)

        st.subheader("Weekday vs Weekend Sales")
        fig, ax = plt.subplots()
        sns.boxplot(x="Weekend", y="Total Sales", data=df, palette="coolwarm", ax=ax)
        st.pyplot(fig)

    with tab4:
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        st.subheader("Sales Distribution by Payment Method")
        payment_sales = df.groupby("Payment")["Total Sales"].sum()
        fig, ax = plt.subplots()
        ax.pie(payment_sales, labels=payment_sales.index, autopct="%1.1f%%", colors=["skyblue", "lightgreen", "orange"])
        ax.set_title("Payment Method Distribution")
        st.pyplot(fig)
