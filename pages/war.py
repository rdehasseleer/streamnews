import streamlit as st
from gnews import GNews
import pandas as pd
KEYWORD = "ukraine"
KEYWORD_FR = "ukraine"
st.markdown("# Main page - Russia vs Ukraine - USA")

news = GNews(language = 'en', period='1d', country="US")
headlines = news.get_news(KEYWORD)    
df = pd.DataFrame(headlines)
st.dataframe(df)
for i, v in df.iterrows():
    article = news.get_full_article(df.iloc[i]['url'])
    st.write(article.text)
    st.header(article.title, anchor=str(i))
    
    st.sidebar.markdown("["+str(article.title)+"](#"+str(i)+")", unsafe_allow_html=True)

st.markdown("# Main page - Russia vs Ukraine - French")

news_fr = GNews(language = 'french', period='1d', country="France")
headlines_fr = news_fr.get_news(KEYWORD_FR)    
df_fr = pd.DataFrame(headlines_fr)
st.dataframe(df_fr)