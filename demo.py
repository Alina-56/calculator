import streamlit as st

# Title of the application
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Dropdown menu for selecting operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation based on selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Display the result
st.write(f"Result: {result}")
