import openai 
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#if openai.api_key is None:
#    print("Error: La clave de API no se cargó correctamente.")
#else:
#    print("Clave de API cargada correctamente.")


#messages = []

#while True:
#    user_input = input("Tú: ")
#    if user_input == "0":
#        break

#    messages.append({"role": "user", "content": user_input})

#    response = openai.Completion.create(
#        model="gpt-4o-mini", 
#        messages=messages
#    )
    
#    responseMessage = response['choices'][0]['message']['content']

#    messages.append({"role": "assistant", "content": responseMessage})

#    print("Lunita EcoAI: " + responseMessage)




#INTERFAZ STREAMLIT

st.title("Lunita EcoAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy Lunita EcoAI, un asistente diseñado para ayudarte. ¿En qué puedo asistirte hoy?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])



if user_input:= st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("role").write(user_input)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )
    responseMessage = response['choices'][0]['message']['content']
    st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
    st.chat_message("assistant").write(responseMessage)
