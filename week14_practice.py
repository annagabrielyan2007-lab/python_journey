# WEEK 14: Introduction to Web UIs with Streamlit

import streamlit as st

# Reuse our Object-Oriented foundation from previous weeks
class UserProfile:
    def __init__(self, name, role, level):
        self.name = name
        self.role = role
        self.level = level
        
    def __str__(self):
        return f"{self.name} ({self.role}) - Level {self.level}"

# --- STREAMLIT FRONTEND INTERFACE ---

st.title("🚀 Python Journey: User Dashboard")
st.write("Welcome to your first interactive web application powered by Python and Streamlit!")

# Sidebar inputs for user interaction
st.sidebar.header("Profile Controls")
input_name = st.sidebar.text_input("Enter Name", "Alex")
input_role = st.sidebar.text_input("Enter Role", "Python Developer")
input_level = st.sidebar.slider("Select Level", 1, 20, 12)

# Create an instance of our class using user input
active_user = UserProfile(input_name, input_role, input_level)

# Display data visually on the main page
st.subheader("Active User Profile")
st.info(str(active_user))

# Interactive button
if st.button("Click to Celebrate Progress!"):
    st.success(f"Awesome job, {input_name}! Your backend OOP logic is now live on the web!")