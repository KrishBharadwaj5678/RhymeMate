import streamlit as st
import requests

st.set_page_config(
    page_title="Rhyme Mate",
    page_icon="icon.png",
    menu_items={
        "About":"RhymeMate is a user-friendly tool that helps you find rhymes for any word you enter. Perfect for poets, songwriters, and anyone looking to add a lyrical touch to their writing. Simply type in a word, and RhymeMate will generate a list of rhyming words in seconds."
    }
)

st.write("<h2 style='color:orange;'>Find Rhymes for Any Word Instantly</h2>",unsafe_allow_html=True)

rhyme=st.text_input("Enter a Word")
btn=st.button("Generate")
if btn:
    word = f'{rhyme}'
    api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
    if response.status_code == requests.codes.ok:
       data=response.json()
       if(len(data)==0):
          st.error("No Rhymes for Your Word")
       else:
        st.write(f"<h3 style=color:#FF69B4;>Words that rhyme with {rhyme}:</h3>",unsafe_allow_html=True)
        # Extracting Unique Rhymes
        unique_rhymes=[]
        for i in data:
           if i not in unique_rhymes:
              unique_rhymes.append(i)
        for j in unique_rhymes:
            st.write(f"""<li style=font-size:22px;>{j}</li>""",unsafe_allow_html=True)