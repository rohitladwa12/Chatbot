# Chatbot
The Ava Chatbot Project is an interactive chatbot using Python (Flask) for backend, HTML/CSS/JS for frontend, and JSON for its knowledge base. It processes user inputs, matches keywords, and returns dynamic responses on topics like cricketers and places, offering an engaging, local, and extensible solution.

--

## Features

- **Keyword-Based Responses**: Recognizes keywords from user inputs to provide relevant answers.
- **Dynamic JSON Knowledge Base**: Uses JSON files to store and retrieve information, making the chatbot easily extensible.
- **Interactive Frontend**: Engaging UI built with HTML, CSS, and JavaScript for seamless user interaction.
- **Lightweight Backend**: Powered by Python Flask for handling API requests.
- **Localized Processing**: Runs entirely on your local machine without external APIs or cloud services.

---

## Technologies Used

### Backend
- **Python**
  - Flask: Framework for handling API requests.
  - NLTK: Tokenizes user input for text processing.

### Frontend
- **HTML/CSS/JavaScript**
  - HTML/CSS: For the chatbot's user interface.
  - JavaScript: Handles API calls and updates the UI dynamically.

### Data Storage
- **JSON Files**: Stores chatbot responses for easy updates and scalability.

### Communication
- **Flask-CORS**: Enables cross-origin requests between frontend and backend.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ava-chatbot.git
   cd ava-chatbot
   ```

2. **Install Dependencies**
   Ensure Python 3.x is installed.
   ```bash
   pip install flask flask-cors nltk
   ```

3. **Run the Backend**
   Navigate to the backend file directory and run the Flask app:
   ```bash
   python First_AI.py
   ```

   The backend will start at `http://127.0.0.1:5000`.

4. **Run the Frontend**
   Open the `Ava_frontend.html` file in a browser or use a live server (e.g., VS Code Live Server extension).

5. **Start Chatting**
   Interact with Ava through the chatbox, and get instant responses.

---

## File Structure

```plaintext
ava-chatbot/
│
├── First_AI.py           # Flask backend for chatbot logic
├── Ava_frontend.html     # Frontend interface for the chatbot
├── contents.json         # JSON file storing response data
└── README.md             # Project documentation
```

---

## How It Works

1. **User Input**:
   - User types a message into the chat interface.
   - The message is sent to the backend via an API call.

2. **Backend Processing**:
   - Flask processes the input, tokenizes it using NLTK, and searches for relevant keywords in the JSON knowledge base.
   - A suitable response is generated and sent back to the frontend.

3. **Frontend Response**:
   - The response is displayed dynamically in the chat interface.

---

## Future Enhancements

- **AI Integration**: Use a pre-trained NLP model like GPT for intelligent responses.
- **Enhanced UI/UX**: Add animations and voice interaction.
- **Scalability**: Extend the knowledge base to include more topics.

---

## License

This project is open-source under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgments

Special thanks to ChatGPT for providing guidance on integrating Flask with a static frontend and using Flask-CORS for smooth communication.
