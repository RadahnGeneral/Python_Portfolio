import streamlit as st

st.set_page_config(layout="wide")

content_contactMe = """
Below you can find some of the apps I have built in Python. Feel free to contact me
"""

col1, col2 = st.columns(2)

with col1:
    st.image("images/GD_profile.png",  )

with col2:
    st.title("Gerard Do")
    info = """ My name is Gerard Do. I majored finance and accounting in university but switched to software development when I was 28. At the time, it was a terrifying decision for me because a lot of people, including my father, believed that I was too old to start learning coding. 
    
    However, I knew at the time technology is the future and coders are the people who participate in the process of building that future. I couldnot resist the temptation of joining, so I made a leap of faith and the rest is history. I love coding now, the enjoyment of solving technical problem,  the thrill of building something from scatch, the mental state of flow that I often immerse myself into, it all make for a great experience as a coder.

    I hope you will like what you see in my porfolio here.
    """
    st.info(info)

st.write(content_contactMe)