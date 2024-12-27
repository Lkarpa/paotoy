import streamlit as st
import pandas as pd

st.header(" Who is going to be your tonight MVP?")

players = {"Ataman": ("https://images.eurohoops.net/2024/02/015542a7-ataman-pao.jpg"),

    "Sloukas": ("https://www.paobc.gr/sites/default/files/"
                       "styles/og_image/public/2024-09/sloukas.png?itok=XZ0V6UXE"),
           "Juancho": ("https://m.basketnews.com/image-392116-crop700x700.jpg"),
           "Grant": ("https://sportstherapy.gr/wp-content/uploads/2023/12/Jerian-Grant.webp"),
           "Nunn" : ("https://images.eurohoops.net/2023/11/"
            "1e7be9ba-kendrick-nunn-looks-profile-panathinaikos.jpg"),
           "Lorenzo Brown" : ("https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn"
               ":ANd9GcRreEjMRvqUzoNuhxmv2s"
               "ellJyEWWlrKYKn3fDeG_d6nSA1TFhQkz8UizSIJsxvHscJN_eTdeAQ4lxvjqU"),
           "Osman" : ("https://upload.wikimedia.org/wikipedia/commons"
             "/thumb/9/92/Cedi_Osman_16_Panathinaikos_BC_20241025_%281%29_%28cropped%29"
             ".jpg/220px-Cedi_Osman_16_Panathinaikos_BC_20241025_%281%29_%28cropped%29.jpg"),
           "Yurtseven" : ("https://upload.wikimedia.org/wikipedia/commons"
                 "/thumb/0/01/%C3%96mer_Yurtseven_77_Panathinaikos_BC_20241025_%281%29.jpg"
                 "/220px-%C3%96mer_Yurtseven_77_Panathinaikos_BC_20241025_%281%29.jpg"),
           "KP": ("https://www.pickngreen.gr/wp-content/uploads/"
          "2024/01/panagiotis-kalaitzakis-official-photo-e1706263509573.jpg")}

st.balloons()

mvp = st.radio('', ['Ataman' ,'Juancho', 'Grant', 'Nunn', 'Sloukas',
                       'Lorenzo Brown', 'Osman', 'Yurtseven', 'KP'], index=0)

if mvp == "Juancho":
    st.write("You selected mine :-) ")
    st.image(players[mvp])
else:
    st.image(players[mvp])
    st.write(mvp)
