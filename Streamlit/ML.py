import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="House Price Predictor")

# Create a title for the app
st.title("House Price Predictor")

# Generate some sample data
np.random.seed(42)
house_size = np.random.randint(1000, 5000, 100)
house_price = house_size * 100 + np.random.normal(0, 10000, 100)

# Create a dataframe
df = pd.DataFrame({'Size (sq ft)': house_size, 'Price': house_price})

# Split the data into training and testing sets
X = df[['Size (sq ft)']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Create a function to make predictions
def predict_price(size):
    return model.predict([[size]])[0]

# Display the sample data
st.subheader("Sample Data")
st.dataframe(df.head())

# Create a scatter plot of the data
st.subheader("House Prices vs Size")
fig, ax = plt.subplots()
ax.scatter(X, y)
ax.set_xlabel('Size (sq ft)')
ax.set_ylabel('Price ($)')
st.pyplot(fig)

# Add a slider for user input
size_input = st.slider("Enter house size (sq ft)", min_value=1000, max_value=5000, value=2500, step=100)

# Make a prediction based on user input
predicted_price = predict_price(size_input)

# Display the prediction
st.subheader("Price Prediction")
st.write(f"Predicted price for a {size_input} sq ft house: ${predicted_price:.2f}")

# Show model coefficients
st.subheader("Model Information")
st.write(f"Intercept: {model.intercept_:.2f}")
st.write(f"Coefficient: {model.coef_[0]:.2f}")

# Create a plot showing the regression line
st.subheader("Regression Line")
fig, ax = plt.subplots()
ax.scatter(X, y)
ax.plot(X, model.predict(X), color='red', linewidth=2)
ax.set_xlabel('Size (sq ft)')
ax.set_ylabel('Price ($)')
st.pyplot(fig)