# client_proposal_writer.py
import streamlit as st
import openai
import os

# ---- Set your OpenAI API key ----
openai.api_key = ("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")  # safer than hardcoding

st.title("Automated Client Proposal Writer")
st.write("Generate professional client proposals in seconds.")

# ---- User Inputs ----
client_name = st.text_input("Client Name")
industry = st.text_input("Industry / Sector")
project_scope = st.text_area("Project Scope / Goals")
budget = st.text_input("Budget (Optional)")
deadline = st.text_input("Deadline / Timeline (Optional)")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Persuasive", "Formal"])

if st.button("Generate Proposal"):
    if client_name and industry and project_scope:
        prompt = f"""
        Write a professional client proposal for {client_name}, a company in the {industry} industry.
        Project Scope / Goals: {project_scope}
        Budget: {budget if budget else 'Not specified'}
        Deadline / Timeline: {deadline if deadline else 'Not specified'}
        Tone: {tone}
        The proposal should include:
        1. Introduction
        2. Project plan / approach
        3. Deliverables
        4. Timeline
        5. Pricing
        6. Call-to-action
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=600
            )
            proposal_text = response.choices[0].message.content.strip()
            st.subheader("Generated Proposal")
            st.text(proposal_text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please fill in Client Name, Industry, and Project Scope.")
