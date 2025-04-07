import streamlit as st

st.title("🧮 BMI Calculator")
st.write("📏 Enter your weight and height to calculate your BMI.")

height = st.number_input(
    "📐 Height (in meters)", min_value=0.5, max_value=3.0, value=1.75)
weight = st.number_input(
    "🏋️ Weight (in kilograms)", min_value=10, max_value=90, value=70)

if st.button("🧠 Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"📊 Your BMI is **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("⚠️ You are underweight. 🍽️")
        elif bmi < 24.9:
            st.success("✅ You have a normal weight. 🥦💪")
        elif bmi < 29.9:
            st.warning("⚠️ You are overweight. 🍔🚶")
        else:
            st.error("🚨 You are obese. 🛑 Please take care! ❤️")
    else:
        st.error("❌ Please enter valid height and weight values.")
