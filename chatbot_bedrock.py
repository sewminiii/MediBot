import streamlit as st
#import backend as backend

# Simulate user preference for displaying chat history (this would come from registration in a real app)
if 'show_chat_history' not in st.session_state:
    st.session_state.show_chat_history = True  # change this true with the backend attribute for preference

# Initialize the session state for chat history if it doesn't already exist
if 'chat_history' not in st.session_state:  # Ensure chat history is properly initialized
    st.session_state.chat_history = []  # Initiate the chat history

# Initialize the file upload variable to avoid errors
uploaded_file = None

# Set up the main layout of the user interface
st.markdown(
    """
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
        }

           
        /* Profile icon styling */
        .sidebar-profile-icon {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            padding: 10px;
            margin-bottom: 10px; 
        }

        .profile-icon {
            cursor: pointer;
            font-size: 24px;
            border: none;
            background: none;
            padding: 0;
        }

        .profile-icon:hover {
            color: #007BFF; /* Change the color on hover */
        }
        .profile-icon {
            cursor: pointer;
            font-size: 24px;
            border: none;
            background: none;
            padding: 0;
            margin-right: 10px;
        }

        .profile-icon:hover {
            color: #007BFF; /* Change the color on hover */
        }

        /* Sidebar styling */
        .sidebar-content {
            display: flex;
            flex-direction: column;
            height: 5vh; /* Adjust height as needed */
            justify-content: flex-start;
            position: relative;
            overflow-y: auto; /* Allow scrolling if content overflows */
            gap: 10px; /* Ensure a small gap between elements */
        }

        .file-upload-container {
            margin: 0; /* Remove any extra margin to ensure tight coupling with chat history */
            padding: 0; /* Remove padding to ensure no unnecessary spacing */
            width: 100%;
        }
    </style>
    <div class="header-container">
        <h1>Interactive Chatbot UI for Healthcare</h1>
    </div>
   
    """,
    unsafe_allow_html=True,
)

# Set up the main layout of the user interface
# st.title("Interactive Chatbot UI for Healthcare")
# if 'memory' not in st.session_state:
#     st.session_state.memory = backend.backend_memory()


# Display chat history and file upload in the sidebar if the user has opted for it during registration (based on backend preference)
if st.session_state.show_chat_history:
    with st.sidebar:
        # Add user profile icon at the top of the sidebar
        st.markdown(
            '''
            <div class="sidebar-profile-icon">
                <button class="profile-icon" onclick="alert('User profile details go here!')">👤</button>
            </div>
            ''',
            unsafe_allow_html=True,
        )

        # Add file upload button statically at the bottom of the chat history panel
        st.markdown('<div class="file-upload-container">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload a medical report or image", type=["jpg", "jpeg", "png", "pdf", "docx"])
        st.markdown('</div>', unsafe_allow_html=True)  # Close the file-upload-container div
        
        st.header("Chat History")
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

        # Display the chat history in the sidebar
        for i, message in enumerate(st.session_state.chat_history):
            role = "👤 User" if message["role"] == "user" else "🤖 MediBOT"
            st.write(f"{role}: {message['text']}")

        st.markdown('</div>', unsafe_allow_html=True)  # Close the sidebar-content div



# Re-render the chat history in the main chat window
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

#add ui chat history to the session cache - session state
if 'chat_history' not in st.session_state: #see if the chat history has not initiated yet
    st.session_state.chat_history = [] #initiate the chat history

# # Initialize the session state for chat history if it doesn't already exist
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []  # Initiate the chat history

#re-render the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Chatbot input box
input_text = st.chat_input("Chat with the MediBOT")

# File upload button to upload medical reports or images
# uploadedx_file = st.file_uploader("Upload a medical report or image", type=["jpg", "jpeg", "png", "pdf", "docx"])

# If a file is uploaded, display its name and add it to the chat history
if uploaded_file is not None:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    with st.chat_message("user"):
        st.markdown(f"**Uploaded file:** {file_details['filename']} ({file_details['filetype']}, {file_details['filesize']} bytes)")

    # Add the file upload details to the chat history (optional)
    st.session_state.chat_history.append({"role": "user", "text": f"Uploaded file: {file_details['filename']}"})

    
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role": "user", "text": input_text})

    placeholder_response = "This is a placeholder response from MediBOT. The actual response will be generated by the backend."
    #chatbot_response = backend.demo_conversation(input_text=input_text, memory=st.session_state.memory)

    with st.chat_message("MediBOT"):
        #  st.markdown(chatbot_response)
        st.markdown(placeholder_response)
    
    st.session_state.chat_history.append({"role": "assistant", "text": placeholder_response})
#   st.session_state.chat_history.append({"role": "assistant", "text": chatbot_response})