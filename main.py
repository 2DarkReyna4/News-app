import streamlit as st
import requests

api_key='2de8cfc469d149ee923e2651c7941866'

st.title("NEWS app")
st.subheader("This application shows the news of a Particular topic")

topic=st.text_input('enter the topic:   ')
limit=st.number_input('How many articles do you require:    ',value=0)

base_url = f"https://newsapi.org/v2/everything?q={topic}&apiKey=daa4b61565614f039bd9c2826c7ba18d"

p={
    'pageSize' : limit,
    'apiKey' : api_key,
    'q' : topic
}

if st.button('Display'):
    result = requests.get(base_url, params=p)

    if result.status_code==200:
        data=result.json()
        articles = data['articles']
        st.subheader("Headlines")
        for news in articles:
            link=news["urlToImage"]
            #st.write(link)
            st.image(link,width=350)
            st.write(f"Source : {news['source']['name']}")
            st.write(f"Author : {news['author']}")
            st.write(f"Headlines : {news['title']}")
            st.write(f"News Description : {news['description']}")
            st.write(f"Link to the article : {news['url']}")
            st.write('\n')
            st.divider()
    else:
        st.error("Enter a valid topic...")
