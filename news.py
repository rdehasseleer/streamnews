import streamlit as st
from gnews import GNews
import pandas as pd

st.markdown("# Streamnews - You shouldn't have to click to see the news...💨")
st.sidebar.markdown("# Streamnews -  Articles 💨")
new = st.text_input("Your search", placeholder="Write the news that you want to know...")

if new:
    news = GNews()# Get news by Keyword
    headlines = news.get_news(new)
    df = pd.DataFrame(headlines)
    for i, v in df.iterrows():
        try:
            article = news.get_full_article(df.iloc[i]['url'])
            st.header(article.title, anchor=str(i))
            st.write(article.text)
            st.sidebar.markdown("["+str(article.title)+"](#"+str(i)+")", unsafe_allow_html=True)
        except AttributeError:
            print("Not accessible:")
            print(v)
    st.write(df)
