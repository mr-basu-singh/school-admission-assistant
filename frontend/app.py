import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="🎓 School Admission Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🎓 School ERP")
st.sidebar.markdown("### Example Questions")

examples = [
    "What is the admission process?",
    "What documents are required?",
    "What is the fee for Grade 5?",
    "Are seats available for Grade 3?",
    "Is transport available in Greater Noida?",
    "What are the school timings?"
]

for q in examples:
    if st.sidebar.button(q):
        st.session_state["question"] = q

# ---------------- Main Page ---------------- #

st.title("🎓 AI School Admission Assistant")
st.caption("Powered by Gemini + RAG + ChromaDB + SQLite")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Read question from sidebar button
question = st.session_state.pop("question", None)

# Or from chat input
chat_input = st.chat_input("Ask your question...")

if chat_input:
    question = chat_input

# ---------------- Handle Question ---------------- #

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    answer = result.get("answer", "No answer returned.")
                    sources = result.get("sources", [])

                else:

                    answer = f"API Error: {response.text}"
                    sources = []

            except Exception as e:

                answer = f"Connection Error:\n\n{e}"
                sources = []

            st.markdown(answer)

            if sources:
                st.divider()
                st.caption("📄 Sources Used")

                for source in sources:
                    st.write(f"• {source}")

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )