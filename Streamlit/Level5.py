##Showing Graphs and charts

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import asyncio

# Set page title
st.set_page_config(page_title="Streamlit Graphs Demo")

async def main():
    st.title("Streamlit Graphs Demo")

    # Generate a simple dataframe
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'Tokyo'],
        'Salary': [50000, 75000, 60000, 65000, 55000]
    })

    # Display the dataframe
    st.subheader("Sample Dataframe")
    st.dataframe(df)

    # Streamlit line chart
    st.subheader("Streamlit Line Chart")
    st.line_chart(df.set_index('Name')['Salary'])

    # Streamlit bar chart
    st.subheader("Streamlit Bar Chart")
    st.bar_chart(df.set_index('Name')['Age'])


    # Matplotlib histogram
    st.subheader("Matplotlib Histogram")
    fig, ax = plt.subplots()
    ax.hist(df['Age'], bins=5, edgecolor='black')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    ax.set_title('Age Distribution')
    st.pyplot(fig)

    # Plotly pie chart
    st.subheader("Plotly Pie Chart")
    fig = px.pie(df, values='Salary', names='Name', title='Salary Distribution')
    st.plotly_chart(fig)

    # Plotly scatter plot
    st.subheader("Plotly Scatter Plot")
    fig = px.scatter(df, x='Age', y='Salary', color='City', size='Salary',
                     hover_data=['Name'], title='Age vs Salary by City')
    st.plotly_chart(fig)

if __name__ == "__main__":
    asyncio.run(main())