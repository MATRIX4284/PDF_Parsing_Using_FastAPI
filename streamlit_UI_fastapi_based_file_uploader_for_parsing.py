import streamlit as st
import streamlit as st
import pandas as pd
from io import StringIO
import requests

url='http://127.0.0.1:8000/uploadfile/'

st.header("PDF Parser")

#detail_option={"option":option}


uploaded_file = st.file_uploader("Choose a file",key='upload_file')
if uploaded_file is not None:
    # To read file as bytes:
    
    bytes_data = uploaded_file.getvalue()
    
    
    files={'file': uploaded_file}
    
    headers={'Content-Type',"multipart/form-data"}
    
    response = requests.post(url,files=files)
    
    print("completed requests")
    
    st.markdown(response)