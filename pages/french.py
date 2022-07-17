import streamlit as st
from gnews import GNews
import pandas as pd

st.markdown("# Main page - Sur quoi voulez vous être informé ? 🎈")
new = st.text_input("Votre recherches", placeholder="")
if new:
    news = GNews(language = 'fr', period='5d', country="FR")
    headlines = news.get_news(new)
    df = pd.DataFrame(headlines)
    st.write(df)
    
    for i, v in df.iterrows():
        article = news.get_full_article(df.iloc[i]['url'])
        st.write(article.text)
        st.header(article.title, anchor=str(i))
        st.sidebar.markdown("["+str(article.title)+"](#"+str(i)+")", unsafe_allow_html=True)
