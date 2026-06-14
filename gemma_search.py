import streamlit as st
import google.generativeai as genai

# 1. Page settings (Makes it look like a search engine)
st.set_page_config(page_title="Gemma Search", page_icon="🔍", layout="centered")

# 2. Custom CSS to style the page
st.markdown("""
    <style>
    .main { text-align: center; }
    div.stButton > button:first-child {
        background-color: #f8f9fa;
        color: #3c4043;
        border: 1px solid #f8f9fa;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Securely connect to Gemma using an API Key
if "GEMMA_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMMA_API_KEY"])
else:
    st.error("Please configure your GEMMA_API_KEY in Streamlit Cloud secrets.")
    st.stop()

# 4. Search Title
st.markdown("<h1 style='text-align: center; color: #4285F4; font-size: 50px;'>Gemma Search</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Ask Gemma anything...</p>", unsafe_allow_html=True)

# 5. Search Bar Input
search_query = st.text_input("", placeholder="Type your question here...", label_visibility="collapsed")

# 6. Search Button
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    search_clicked = st.button("Search")

# 7. Show Real AI Results
if search_query and search_clicked:
    st.markdown("---")
    with st.spinner("Gemma is thinking..."):
        try:
            # Call Gemma 2 model
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Act like an AI search engine. Provide a structured, clear summary answering this query: {search_query}"
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🔍 Search Results for: *{search_query}*")
            st.write(response.text)
        except Exception as e:
            st.error(f"Search failed: {e}")
