import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

import os 
from dotenv import load_dotenv

api_key=st.secrets("BotApi")

# load_dotenv()
# api_key=os.getenv("BotApi")


model = ChatGroq(model="llama-3.1-8b-instant",api_key=api_key )


system_prompt = SystemMessage(
    content='''
        You are an Upwork proposal description generator. You will take two inputs:
        - Job Description 
        - Profile Description of the applicant.

        your task is to make a propsal based on the job description using applicant profile.
        Use hookup relevant from the job for the attention of client , also dont mention all the 
        skills in the profile, just list those who are realtable and relevant to the job.
        After the hookup tell them about the project approach that how you will carry the project
        Dont add extra information. Keep it concise but eye catching.
        just tell them about what you bring to the table with your skills.
        Tell them which tools will be use in the project accordigng to the job description. 
        If the client ask for any question in teh job answer them in a professional way dont use extra words
        Your main focus will be the client problem and how you will respond to the problem with best solution.
        Make sure that the client will be satisfied with our proposal.
        Dont forget to Call To Action.
    '''
)

# UI layout
st.set_page_config(page_title="Upwork Proposal Generator", layout="centered")

st.title("📝 Upwork Proposal Generator")
st.markdown("Generate professional proposals with AI!")

# Input fields
job_desc = st.text_area("📄 Job Description", height=250)
profile_desc = st.text_area("🧑‍💼 Applicant Profile Description", height=250)

# When user clicks the button
if st.button("Generate Proposal"):
    if job_desc.strip() == "" or profile_desc.strip() == "":
        st.warning("Please enter both the job description and the profile description.")
    else:
        with st.spinner("Generating proposal..."):
            # Combine the inputs
            user_input = f"Job Description: {job_desc}\n\nApplicant Profile: {profile_desc}"
            # Get the AI-generated response
            response = model.invoke([
                system_prompt,
                HumanMessage(content=user_input)
            ])
            st.success("✅ Proposal Generated:")
            st.text_area("📝 Your Proposal", value=response.content, height=500)


