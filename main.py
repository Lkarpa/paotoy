import streamlit as st

mvp = st.radio(
    "Who is going to be your tonight MVP?",
    ['Juancho', 'Grant', 'Nunn', 'Sloukas',
     'Lorenzo Brown', 'Osman', 'Jurtseven', 'KP']
)

if mvp == "Juancho":
    st.write("You selected mine :-) ")
else:
    st.write(mvp)