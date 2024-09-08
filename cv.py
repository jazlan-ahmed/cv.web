import streamlit as st
from PIL import Image

img = Image.open("WhatsApp Image 2024-05-06 at 5.34.40 PM.jpeg")
st.title("Saqib Mehmood")

col1, col2 = st.columns(2)
with col1:
    st.image(img, width = 150)
    st.header("PERSONAL INFORMATION")
    st.markdown("""
    Father Name : **Nasir Mehmood**\n
    Date of Birth : **19-05-2003**\n
    CNIC NO : **41102-7502546-1**\n
    Domicile/PRC : **District Badin**\n
    Marital Status : **Single**\n
    Nationality : **Pakistani**
                """)
    
    st.header("ACADEMIC QUALIFICATION")
    st.write("""
    - Matriculation : Grade A\n
       **Year : 2019**
             
    - Intermediate : Grade A1\n
       **Year : 2021**
             """)

with col2:
    st.header("OBJECTIVE")
    st.write("TO WORK WITH A WELL REPUTED ORGANIZATION WHERE I CAN USE MY KNOWLWDGE AND STRENGTHS FOR THE BETTERMENT OF NOT ONLY MY FUTURE BUT ALSO FOR THE BETTERMENT OF ORGANIZATION.")

    st.header("Skills")
    st.write("""
    - Self-motivation, initiative with a high level of energy.
    - Able to inspire, comfort, build, self-esteem.
    - Excellent communicaton skill.
    - Stress and time management ability.
    - Skillfull in the management.
             """)
    
    st.header("Languages")
    st.write("""
    - **English**
    - **Sindhi**
    - **Urdu**
""")
    st.progress(80)
    st.progress(92)
    st.progress(98)
    
    st.header("Contact")
    st.write("Address : **Ward No 02 Near National Bank Golarchi Taluka S.F.Rahu (Golarchi) District Badin**")
    st.write("Phone : **0348-3260978**")



