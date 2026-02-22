import streamlit as st

# MUST BE FIRST: Setup the page appearance
st.set_page_config(page_title="EduVixenAK", page_icon="🦊", layout="wide")

# Sidebar Navigation for all 10 Tools
st.sidebar.title("🦊 EduVixenAK")
st.sidebar.markdown("---")
menu = [
    "🏠 Dashboard", 
    "📺 Presentation Gen", 
    "📝 Quiz Creator", 
    "📄 Paper Maker", 
    "🔍 Paper Checker", 
    "📊 Classroom Data", 
    "📧 Admin Assistant", 
    "🌿 Mind Map & Flow", 
    "🗂️ Flash Cards", 
    "👁️ Smart Visual Assistant", 
    "📂 My Projects"
]
choice = st.sidebar.radio("Select a Tool", menu)

# --- HOME DASHBOARD ---
if choice == "🏠 Dashboard":
    st.title("Welcome to EduVixenAK")
    st.write("Your all-in-one AI teaching ecosystem is online.")
    
    # Visual Status Cards
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🚀 Quick Start\nSelect a tool from the sidebar to begin generating content.")
    with col2:
        st.success("### 📂 Project Safety\nAll generations are automatically tracked in your 'My Projects' folder.")

# --- TOOL PLACEHOLDERS (We will fill these next) ---
else:
    st.title(choice)
    st.info(f"The {choice} module is ready. Which feature should we code first?")
