import streamlit as st
with  st.sidebar:
    st.title("HONRAA!", anchor='🤖')
    st.write("One step at a time, we will get there!")
    st.divider()
    st.subheader('Session Stats')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Messages')
        st.subheader('1')
    with col2:
        st.subheader('Total')
        st.subheader('1')
    st.divider()
    
    st.subheader('Controls')
    options = st.selectbox('Accent', ['Cameroon', 'Egypt', 'Burkina Faso', 'Ghana', 'Nigeria'])
    st.slider('Model Temperature', 0.0, 2.0, 1.0)

st.header('Chat with HonraAI', anchor='chat')
with st.chat_message("user", avatar="🙂"):
    st.write("Hello")
with st.chat_message("assistant", avatar="😶‍🌫️"):
    st.write("Hello there! i'm HonraAI, your friendly and informative assistant specialise in heart disease i'm here to help you with questions about heart health, conditions and risk factors. How can I assist you today?")
    st.button('Read aloud')
st.divider()
st.chat_input('Message HonraAI...')