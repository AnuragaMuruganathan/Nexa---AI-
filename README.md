# 🤖 Mistral AI Chat Application

A powerful generative AI application built with Mistral model through Ollama, LangChain, and Streamlit. Experience local AI conversations with full privacy and customization.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FF6B35?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-00ADD8?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **💬 Intelligent Chat**: Conversational AI with Mistral model
- **🎯 Multiple Modes**: Chat, creative writing, and code assistance
- **🧠 Memory Context**: Remembers conversation history
- **🔒 Local & Private**: Runs entirely on your machine
- **🎨 Beautiful UI**: Clean Streamlit interface
- **⚡ Real-time Responses**: Fast AI interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed
- Mistral model downloaded

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mistral-ai-app.git
   cd mistral-ai-app

2. **Install dependencies**:
   ```bash
    pip install -r requirements.txt
   
3. **Set up Ollama (if not already done)**:
   ```bash
    # Install Ollama from https://ollama.ai/
    # Pull Mistral model
    ollama pull mistral
   
4. Run the application:
   ```bash
    streamlit run app.py
    Open your browser and go to http://localhost:8501

## 🎮 How to Use

### 💬 Chat Mode

- Have natural conversations with Mistral AI

- Conversation history is maintained throughout the session

- Perfect for Q&A, brainstorming, and general assistance

### ✍️ Creative Writing Mode

- Generate stories, poems, essays, and blog posts

- Choose from different writing styles

- Provide topics and let AI do the creative work

### 💻 Code Assistant Mode

- Get help with programming tasks

- Support for multiple languages (Python, JavaScript, Java, etc.)

- Generate clean, commented code snippets

## ⚙️ Configuration

### Environment Variables (Optional)

**Create a .env file for custom settings**:
env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral

## Model Settings

**Adjust temperature and other parameters in app.py**:

python
llm = Ollama(
    model="mistral",
    temperature=0.7,  # Creativity level (0.0-1.0)
    top_p=0.9         # Diversity control
)

## 🛠️ Customization

### Adding New Features

- **New AI Chains**: Extend the EnhancedMistralApp class

- **UI Modifications**: Edit the Streamlit components in app.py

- **Additional Models**: Add new Ollama models in the initialization

### Example: Adding a Translation Chain
python
translation_prompt = PromptTemplate(
    input_variables=["text", "target_language"],
    template="Translate this text to {target_language}: {text}"
)

## 🤝 Contributing

### We welcome contributions! Please feel free to:

- Fork the project

- Create a feature branch (git checkout -b feature/amazing-feature)

- Commit your changes (git commit -m 'Add amazing feature')

- Push to the branch (git push origin feature/amazing-feature)

- Open a Pull Request

## 📝 License
### This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting
### Common Issues
1. **Ollama connection failed**

bash
# Ensure Ollama is running:
ollama serve

2. **Model not found**

bash
# Download the Mistral model:
ollama pull mistral
3. **Port already in use**

bash
# Change Streamlit port:
streamlit run app.py --server.port 8502


### Getting Help
- Check Ollama documentation

- Review Streamlit docs

- Explore LangChain guides

### 🙏 Acknowledgments
- Mistral AI for the powerful language model

- Ollama for local model management

- LangChain for AI orchestration

- Streamlit for the web framework

⭐ If you find this project useful, please give it a star on GitHub!

<div align="center">
Built with ❤️ using Python, LangChain, and Streamlit

Report Bug · Request Feature

</div> ```
