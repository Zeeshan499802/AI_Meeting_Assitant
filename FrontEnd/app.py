import streamlit as st
import requests

# API_URL = "http://127.0.0.1:8000"
API_URL = "https://ai-meeting-assitant-63ne.onrender.com"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 AI Video Intelligence Assistant")

# ---------------- INPUT ----------------
st.subheader("📌 Input Video")
source = st.text_input("Enter Video URL or File Path")
language = st.selectbox("Language", ["en", "ur"])

# ---------------- PROCESS ----------------
if st.button("🚀 Process Video"):

    if not source:
        st.error("Please enter video URL")
    else:
        with st.spinner("Processing video... ⏳"):

            res = requests.post(
                f"{API_URL}/process",
                json={"source": source, "language": language}
            )

            if res.status_code == 200:
                st.session_state.data = res.json()
                st.success("Processing Completed!")
            else:
                st.error(res.text)

# ---------------- DATA ----------------
data = st.session_state.get("data")

if data:

    st.divider()

    # ---------------- TITLE ----------------
    st.subheader("📝 Title")
    st.info(data.get("title", ""))

    # ---------------- SUMMARY ----------------
    st.subheader("📄 Summary")

    summary = data.get("video_summary", "")
    for line in summary.split("."):
        if line.strip():
            st.write("🔹 " + line.strip())

    # ---------------- TRANSCRIPT ----------------
    with st.expander("📜 Full Transcript"):
        st.text_area("", data.get("transcript", ""), height=300)

# ---------------- RAG CHAT ----------------
st.divider()
st.subheader("💬 Ask Questions (RAG)")

if data:

    question = st.text_input("Ask something from video")

    if st.button("Ask"):

        res = requests.post(
            f"{API_URL}/ask",
            json={
                "transcript": data.get("transcript", ""),
                "question": question
            }
        )

        if res.status_code == 200:
            st.success(res.json()["answer"])
        else:
            st.error(res.text)

else:
    st.info("Process video first to enable Q&A")