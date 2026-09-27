# WEEK 15: Advanced Streamlit Layouts and Multi-User Dashboards

import streamlit as st

# 1. Our OOP Foundation
class TeamMember:
    def __init__(self, name, role, experience_years):
        self.name = name
        self.role = role
        self.experience_years = experience_years

    def to_dict(self):
        # Convert object attributes to a dictionary for tabular display
        return {
            "Name": self.name,
            "Role": self.role,
            "Experience (Years)": self.experience_years
        }

# Page configuration
st.set_page_config(page_title="Team Dashboard", layout="wide")

st.title("👥 Advanced Team Management Dashboard")
st.write("Welcome to Week 15! Let's organize data using columns and tables.")

# 2. Sidebar Controls for Adding Team Members
st.sidebar.header("Add New Team Member")
new_name = st.sidebar.text_input("Name", "Jordan")
new_role = st.sidebar.selectbox("Role", ["Developer", "Designer", "Data Scientist", "Manager"])
new_exp = st.sidebar.slider("Experience (Years)", 1, 15, 3)

# Initialize a session state list to store team members across interactions
if "team_members" not in st.session_state:
    st.session_state.team_members = [
        TeamMember("Alex", "Developer", 5),
        TeamMember("Sam", "Designer", 3)
    ]

# Add button logic
if st.sidebar.button("Add Member"):
    st.session_state.team_members.append(TeamMember(new_name, new_role, new_exp))
    st.success(f"Added {new_name} to the team!")

# 3. Layout using Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Team Overview Metrics")
    total_members = len(st.session_state.team_members)
    st.metric(label="Total Team Size", value=total_members)

with col2:
    st.subheader("🔍 Quick Search / Filter")
    selected_role = st.selectbox("Filter by Role", ["All"] + list(set(m.role for m in st.session_state.team_members)))

# 4. Displaying Data in a Table (`st.dataframe`)
st.subheader("📋 Active Team Directory")

# Filter members based on selection
if selected_role == "All":
    filtered_list = st.session_state.team_members
else:
    filtered_list = [m for m in st.session_state.team_members if m.role == selected_role]

# Convert objects to dictionaries for the dataframe
data_table = [member.to_dict() for member in filtered_list]
st.dataframe(data_table, use_container_width=True)