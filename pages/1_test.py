import streamlit as st
import openai
from openai import OpenAI
import requests
import time

client = OpenAI(st.secrets.OPENAI_API_KEY)
assistantid = "asst_Eg9pwdwnWRWK1TPP8JpcVPAo"
pa_email_url = "https://prod-25.westeurope.logic.azure.com:443/workflows/a40bd2920a66479eb1f1a7a51339b4ee/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=72dF_uTi9SBcZgybC-Mg8SJdP3zYM-KgRDxJdZgl_4I"
threadid = client.beta.threads.create().id

def runassistant(varThread, varAssistant, varMessage):
    message = """
    Create the json email output for the following:
    
    {varMessage}
    
    Reminder: JSON ONLY
    """
    
    msg = client.beta.threads.messages.create(
        thread_id=threadid, 
        content=message,
        role="user"
    )
    
    run = client.beta.threads.runs.create(
        assistant_id=assistantid,
        thread_id=threadid
    )
    
    while run.status == "in_progress" or run.status == "queued": 
       time.sleep(1)
       run = client.beta.threads.runs.retrieve(
           run_id=run.id,
           thread_id=threadid
       ) 
       
       if run.status == "completed":
           msgs = client.beta.threads.messages.list(
               thread_id=threadid
           )
           
           msgs_data = msgs.data
                      
           return msgs_data


if prompt:=st.chat_input("prompt"):
    m = runassistant(threadid, assistantid, prompt)
    for messag in m:
        role = messag.role
        content = messag.content[0]
        content1 = content.text.value
        
        response = requests.post(url = pa_email_url, json=content1)
        
        with st.chat_message(role):
            st.markdown(content1)
    
