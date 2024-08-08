import streamlit as st

# Function to get the chatbot response (for now, it just echoes the input)
def get_chatbot_response(user_input):
    # Placeholder for a more advanced chatbot response
    return f"You said: {user_input}"

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Title of the app
st.title("Chatbot")

# Display chat history
st.subheader("Chat History")
for message in st.session_state.chat_history:
    st.write(message)

# User input section at the bottom within a form
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You: ", placeholder="Type your message here...")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    response = get_chatbot_response(user_input)
    st.session_state.chat_history.append(f"You: {user_input}")
    st.session_state.chat_history.append(f"Bot: {response}")
    st.session_state.user_input = ''  # Clear the user input

    # Rerun to update the chat history
    st.rerun()
