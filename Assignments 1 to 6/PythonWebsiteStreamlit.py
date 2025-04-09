import streamlit as st

st.title("🧮 Simple Calculator")
st.write("🔢 Enter two numbers and select an operator to perform the calculation.")

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "❌ Cannot divide by zero"
        return num1 / num2
    else:
        return "⚠️ Invalid operator"

num1 = st.number_input("✏️ Enter first number:", value=0)
num2 = st.number_input("✏️ Enter second number:", value=0)
operator = st.radio("➕➖✖️➗ Select operator", ("add ➕", "subtract ➖", "multiply ✖️", "divide ➗"))

# Convert emoji label to symbol
symbol_map = {
    "add ➕": "+",
    "subtract ➖": "-",
    "multiply ✖️": "*",
    "divide ➗": "/"
}

if st.button("🧮 Calculate"):
    result = calculator(num1, num2, symbol_map[operator])
    st.write(f"✅ The result is: **{result}**")
