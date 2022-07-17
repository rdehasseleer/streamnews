import streamlit as st
from gnews import GNews
import pandas as pd
KEYWORD = "python"
KEYWORD_FR = "python"
st.markdown("# Main page - Python")

news = GNews(language = 'en', period='1d', country="US")
headlines = news.get_news(KEYWORD)    
df = pd.DataFrame(headlines)
st.dataframe(df)
for i, v in df.iterrows():
    article = news.get_full_article(df.iloc[i]['url'])
    st.write(article.text)
    st.header(article.title, anchor=str(i))
    
    st.sidebar.markdown("["+str(article.title)+"](#"+str(i)+")", unsafe_allow_html=True)

st.markdown("# Main page - Python")
