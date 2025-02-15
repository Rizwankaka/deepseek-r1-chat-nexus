# 🤖 Deepseek Reasoning Chat Interface Collection

A collection of different chat interfaces for interacting with the DeepseekR1 language model through Ollama. Features multiple UI options including Gradio, Streamlit, and Chainlit! 

## ✨ Features

- 🎯 **Multiple UI Options**:
  - 🚀 Gradio - Modern, responsive chat interface
  - 📊 Streamlit - Clean, data-app style interface
  - ⚡ Chainlit - Professional chat experience

- 🔄 **Real-time Streaming**: Watch the AI think and respond in real-time
- 💬 **Chat History**: Maintains conversation context
- 🎨 **Clean Interface**: User-friendly design across all platforms

## 🛠️ Installation

### Prerequisites

- Python 3.11+ 
- [Ollama](https://ollama.com/) installed and running
- Deepseek model pulled in Ollama

### 1️⃣ Clone the Repository

git clone https://github.com/Rizwankaka/deepseek-r1-chat-nexus

cd deepseek-r1-chat-nexus

### 2️⃣ Create Virtual Environment
#### Using conda
conda create -p venv python==3.11 -y

conda activate venv/

#### OR using venv
python -m venv venv
#### For Windows
.\venv\Scripts\activate
#### For Unix/MacOS
source venv/bin/activate

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Pull the Deepseek Model
```bash
ollama pull deepseek-r1:1.5b
```
## 🚀 Running the Applications

### Gradio Interface
```bash
python gradio.py
```
- 🌐 Opens a web interface at `http://localhost:7860`
- 💻 Features a clean chat interface with streaming responses
- 🔄 Includes message history and clear chat function

### Streamlit Interface
```bash
streamlit run streamlit.py
```
- 🎯 Opens at `http://localhost:8501`
- 📱 Responsive design
- 📝 Persistent chat history during session

### Chainlit Interface
```bash
chainlit run chainlit.py
```
- ⚡ Modern, professional chat interface
- 🔥 Real-time streaming responses
- 📊 Enhanced UI elements

## 📦 Dependencies

```txt
ollama==0.4.7
gradio==5.14.0
streamlit==1.39.0
chainlit==2.1.0
```
## 💡 Tips

- Make sure Ollama is running in the background before starting any interface
- Each interface can be run independently
- Choose the interface that best suits your needs:
  - Gradio: For a simple, lightweight chat interface
  - Streamlit: For a data-app style experience
  - Chainlit: For a professional chat application

## 🔧 Troubleshooting

- If you encounter any errors, ensure:
  1. Ollama is running (`ollama serve`)
  2. The Deepseek model is properly pulled
  3. Your virtual environment is activated
  4. All dependencies are correctly installed

## 🤝 Contributing

Feel free to:
- 🐛 Report bugs
- 💡 Suggest enhancements
- 🔀 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Rizwankaka/deepseek-r1-chat-nexus/blob/main/LICENSE) file for details.

---
Made with ❤️ by Rizwan Rizwan

