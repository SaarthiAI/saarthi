import streamlit as st

from .langchain import get_conversation_chain
from .htmlTemplates import css, bot_template, user_template

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def load_ui(vectorstore):
    st.set_page_config(page_title="Ministry of coal", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    st.header("Welcome to Ministry of Coal PDFs :books:")

    user_question = st.text_input("Ask a question about mining industry:")
    if user_question:
        handle_userinput(user_question)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.session_state.conversation = get_conversation_chain(vectorstore)
