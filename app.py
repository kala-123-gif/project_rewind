import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Project Rewind",
    page_icon="🧠",
    layout="wide"
)

# Application title
st.title("🧠 PROJECT REWIND")

st.subheader("Your Personal AI Context Intelligence System")

st.write(
    "Never lose your progress. "
    "Never waste time restarting."
)

st.divider()

# Sidebar
st.sidebar.title("PROJECT REWIND")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "My Projects",
        "Add Memory",
        "Smart Search",
        "Project Rewind",
        "Recommendations",
        "Memory Integrity",
        "Analytics"
    ]
)

# Dashboard
if page == "Dashboard":

    st.header("Welcome Back!")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Active Projects", 0)
    col2.metric("Total Memories", 0)
    col3.metric("Pending Tasks", 0)
    col4.metric("Completed Tasks", 0)

    st.divider()

    st.subheader("Your Workspace")

    st.info(
        "Create your first project to start "
        "building your intelligent memory."
    )

    st.subheader("How Project Rewind Works")

    st.write("1. Create your project.")

    st.write("2. Record your daily activities.")

    st.write("3. Search previous memories using AI.")

    st.write("4. Recover your previous working context.")

    st.write("5. Get intelligent next-step recommendations.")

# Other pages: temporary placeholders
else:

    st.header(page)

    st.info(
        "This module will be implemented "
        "in the upcoming development phase."
    )

    
