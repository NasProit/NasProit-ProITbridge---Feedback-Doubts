import streamlit as st
import webbrowser
from url import FORM_LINKS, FEEDBACK_URL

# Load CSS
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS styles
load_css()

# App Title with Logo

st.markdown('<p class="title">✨ ProITbridge - Feedback & Doubts ✨</p>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 📌 Navigation")
selected_tab = st.sidebar.radio("Go to:", ["📝 Feedback", "❓ Doubts"])

# Add a horizontal line for separation
st.markdown("<hr style='border:1px solid #000000;'>", unsafe_allow_html=True)

# Feedback Section
if selected_tab == "📝 Feedback":
    st.markdown('<p class="header">📝 Feedback</p>', unsafe_allow_html=True)
    
    if st.link_button("✍️ Submit Feedback"):
        webbrowser.open_new_tab(FEEDBACK_URL)

# Doubts Section
elif selected_tab == "❓ Doubts":
    st.markdown('<p class="header">❓ Doubts</p>', unsafe_allow_html=True)
    topic = st.selectbox("📚 Select a topic", list(FORM_LINKS.keys()))

    if st.button(f"🚀 Ask Doubt in {topic}"):
        webbrowser.open_new_tab(FORM_LINKS[topic])
