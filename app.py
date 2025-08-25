import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import os

# Set page configuration
st.set_page_config(
    page_title="Mistral AI Chat",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

class MistralChatApp:
    def __init__(self):
        self.llm = None
        self.chain = None
        self.initialize_llm()
    
    def initialize_llm(self):
        """Initialize the Mistral model from Ollama"""
        try:
            # Connect to Ollama's Mistral model
            self.llm = Ollama(
                model="mistral",
                base_url="http://localhost:11434",  # Default Ollama URL
                temperature=0.7,
                top_p=0.9
            )
            
            # Create prompt template
            prompt_template = PromptTemplate(
                input_variables=["history", "human_input"],
                template="""You are a helpful AI assistant. Use the following conversation history and current input to provide a helpful response.

Conversation History:
{history}

Current Input: {human_input}

Assistant Response:"""
            )
            
            # Create chain with memory
            self.chain = LLMChain(
                llm=self.llm,
                prompt=prompt_template,
                memory=st.session_state.memory,
                verbose=True
            )
            
        except Exception as e:
            st.error(f"Error initializing Mistral model: {e}")
    
    def get_response(self, user_input):
        """Get response from Mistral model"""
        try:
            if self.chain:
                response = self.chain.run(human_input=user_input)
                return response
            else:
                return "Model not initialized. Please check your Ollama setup."
        except Exception as e:
            return f"Error generating response: {e}"

def main():
    st.title("🤖 Mistral AI Chat Assistant")
    st.markdown("Chat with your local Mistral model powered by Ollama")
    
    # Initialize the chat app
    if "chat_app" not in st.session_state:
        st.session_state.chat_app = MistralChatApp()
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        if st.button("🔄 Clear Chat History"):
            st.session_state.messages = []
            st.session_state.memory.clear()
            st.rerun()
        
        st.divider()
        st.subheader("About")
        st.info("""
        This app uses:
        - Mistral model via Ollama
        - LangChain for AI orchestration
        - Streamlit for the web interface
        """)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to ask?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_app.get_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()