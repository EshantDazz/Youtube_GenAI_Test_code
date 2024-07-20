import streamlit as st
import pandas as pd
import numpy as np
import asyncio

# Set page title - this must be the first Streamlit command
st.set_page_config(page_title="Streamlit Tables and Metrics Demo")

async def main():
    st.title("Streamlit Tables and Metrics Demo")

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

    # Display table
    st.subheader("Sample Table")
    st.table(df.head(3))

    # Display metrics
    st.subheader("Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Average Age", value=f"{df['Age'].mean():.1f}")
    with col2:
        st.metric(label="Total Salary", value=f"${df['Salary'].sum():,}")
    with col3:
        st.metric(label="Number of Employees", value=len(df))



if __name__ == "__main__":
    asyncio.run(main())