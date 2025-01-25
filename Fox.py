import streamlit as st
import requests
st.markdown(
    """
        <style>
            [data-testid="stAppViewContainer"]{
                background-image:url("https://images.freeimages.com/images/large-previews/cc8/natural-forest-sunburst-1337301.jpg");
                background-size:cover;
                background-repeat:no-repeat;
                background-attachment:fixed;
                color:white;
            }
            .fox-container{
                position:fixed;
                bottom:30px;
                left:30px;
                display:flex:

            }
            .text-box{
                background-color:blue;
                border-radius:10px;
                margin-bottom:20px;
                max-width:600px;
                padding:10px;
                text-align:center;
                justify-content:center;
            }
        </style>
""" ,
unsafe_allow_html=True
)
st.markdown("""
    <div class="text-box">
        <h1>🦊Fox Generator</h1>
        <p>A fox generator that spawns 1 fox as your pet. You have to take care of it and find resources to feed it and create a shelter.</p>
   </div>
""",
unsafe_allow_html=True)
if st.button("Click here for a fox."):
    try:
        response=requests.get("https://randomfox.ca/floof/")
        if response.status_code==200:
            fox_data=response.json()
            fox_image=fox_data.get("image","https://via.placeholder.com/150")
            st.markdown(
                f"""
                    <div class="fox-container">
                        <img src="{fox_image}" width="150">
                    </div>
                """ ,
                unsafe_allow_html=True
            )
        else:
            st.error("There has been a problem in getting your fox. Please try again.")
    except Exception as e:
        st.error("error")