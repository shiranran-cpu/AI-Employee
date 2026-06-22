import streamlit as st

from workflows.startup import StartupWorkflow

workflow = StartupWorkflow()

st.title("🏢 AI Employee")

idea = st.text_area(
    "Describe your startup"
)

if st.button("Build"):

    result = workflow.run(idea)

    st.subheader("PRD")
    st.write(result["prd"])

    st.subheader("Design")
    st.write(result["design"])

    st.subheader("Frontend")
    st.code(result["frontend"])

    st.subheader("Backend")
    st.code(result["backend"])
