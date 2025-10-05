# AI Health Assistant

AI Health Assistant is a web-based AI chatbot that provides general health advice using state-of-the-art NLP models from Hugging Face. This project demonstrates Python programming, AI/ML, NLP, and web deployment skills with a clean, interactive interface built using Gradio. Developed and tested in PyCharm for a streamlined workflow.

## Features

- **AI-Powered Health Responses**: Answers general health questions using AI-generated responses.
- **User-Friendly Interface**: Clean and responsive UI built with Gradio and custom CSS styling.
- **Advanced NLP Model**: Powered by `microsoft/phi-1.5` model from Hugging Face.
- **Local Deployment**: Runs entirely on your local machine for privacy and performance.

## Technologies Used

- **Backend**: Python
- **AI Model**: Hugging Face's `microsoft/phi-1.5`
- **Web Interface**: Gradio
- **Development Environment**: PyCharm

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11 or higher
- pip (Python package installer)
- PyCharm (for development and testing)

### Installation

1. **Clone the repository**:

1. **Clone the repository** to your PC:

```bash
git clone https://github.com/nehavwk222/AI-Health-Assistant.git
Open the project folder in PyCharm.

Create a virtual environment (if not already created). In PyCharm:

Go to File > Settings > Project: <project_name> > Python Interpreter

Click ⚙️ → Add... → New environment

Choose Python version and create.

Install dependencies (if using requirements.txt):

bash
Copy code
pip install -r requirements.txt
Run the main application from the PyCharm terminal:

powershell
Copy code
# Navigate to the project folder (adjust path if needed)
cd <path_to_your_project_folder>

# List Python files (optional, just to check)
dir *.py

# Run the Gradio app
python gradio_app.py
Access the app:

Open a browser and go to the local URL displayed in the terminal, usually:

cpp
Copy code
http://127.0.0.1:7860

![AI Health Assistant Interface](https://github.com/nehavwk222/AI-Health-Assistant/blob/main/Screenshot%202025-09-09%20165054.png)
