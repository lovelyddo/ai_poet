#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써줘.")
# print(result.content)

#streamlit은 페이지를 만들어줌
import streamlit as st

st.title("AI야, 시를 써줘!")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("입력한 시의 주제 : " + subject)


if st.button("시 작성"):
    with st.spinner("시 작성중 ...") :
        result = chat_model.invoke(subject + "에 대한 시를 써줘.")
        st.write(result.content)