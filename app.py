import streamlit as st
from google import genai  




GOOGLE_API_KEY = st.secrets["AIzaSyCL8D8C28ZiXbyygIEJ0glLUPdrCTzFayE"]


client = genai.Client(api_key=GOOGLE_API_KEY)


st.set_page_config(page_title="AI Fake News Detector")
st.title("🔍 Fake News Detector")
st.write("Analyze articles using **Gemini 3 Flash**.")

news_input = st.text_area("Article Content:", height=250)

if st.button("Check Authenticity", type="primary"):
    if not news_input.strip():
        st.warning("Please paste some text first.")
    else:
        try:
            with st.spinner("Analyzing..."):
                
                prompt_text = (
                    "Act as a professional fact-checker. Determine if the following "
                    "news is REAL, FAKE, or MISLEADING. Provide a detailed explanation "
                    f"for your verdict.\n\nTEXT: {news_input}"
                )
                
                
                response = client.models.generate_content(
                    model="gemini-3-flash-preview", 
                    contents=prompt_text
                )
                
                st.subheader("Analysis Result")
                st.info(response.text)
                
        except Exception as e:
           
            st.error(f"Error: {e}")



