import streamlit as st
import google.generativeai as genai
from PIL import Image
import os



st.set_page_config(page_title="HelmetGuard AI", page_icon="🛡️", layout="centered")
os.environ["GOOGLE_API_KEY"]="AIzaSyAk3XfMjeiivTSZ9MYHNMmHetTV7GR_Ar0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-2.0-flash")



tab1,tab2=st.tabs(["About","HelmetGuard AI"])
with tab1:
    st.markdown("""🛡️ HelmetGuard AI – Smart Helmet Detection App
by Soumendu Das

Stay safe, stay smart! HelmetGuard AI is an AI-powered image analysis tool designed to detect helmets in images with speed and accuracy. This app helps ensure safety compliance across various fields like construction, transportation, and more.

🔧 How it works:
Just upload an image, and HelmAI will instantly check if a helmet is present – giving you a clear “yes” or “no” response using advanced machine learning.

""")
    st.text("""✨ Features:

    Fast and accurate helmet detection

    Simple and clean UI for easy uploads

    Powered by Google Gemini’s advanced vision model

    Built with ❤️ by Soumendu Das

    Ideal for:

    Construction safety monitoring

    Traffic enforcement projects

    Workplace compliance checks

    AI and computer vision research
""")

with tab2:    
  st.title("🛡️ HelmetGuard AI")
  on=st.toggle("Camera")
  if on:
      uploaded_image=st.camera_input("Take photo")
  else : uploaded_image=st.file_uploader("📷 Upload an image to check for a helmet",type=["jpg", "jpeg", "png"])
  search_object="helmet"

  with st.spinner("Analyzing image..."):
    if uploaded_image:
        image=Image.open(uploaded_image)
        col1,col2,col3=st.columns(3,gap='medium')
        with col2:
           st.image(image,caption="Uploaded Image",width=200)
        response=model.generate_content([
         search_object,
         image,
        
          ])

    
        if search_object.lower() in response.text:
                st.success("✅ Helmet detected!")
        else:
            prompt=f"""
            Based on the following description, determine whether a person is wearing a helmet. Answer only with 'Yes' or 'No'. Do not assume anything that is not clearly mentioned. Description: {response.text}"""
            
            final_response=model.generate_content(prompt)
            if final_response=="yes":st.success("✅ Helmet detected!")
            else: st.error("❌ No helmet detected.")