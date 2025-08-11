Real Estate Interactive Chatbot
===============================

An interactive AI-powered **Real Estate Chatbot** built with Flask, HTML, CSS, and JavaScript, using the OpenAI API for smart and natural conversations.  
This chatbot is designed to assist users with real estate-related queries — such as property listings, market trends, buying/selling guidance, and more — in a conversational way.

------------------------------------------------------------
Project Status
------------------------------------------------------------
🚧 This project is currently in active development.  
Core functionalities are operational, but certain planned features and optimizations are still being implemented. Expect frequent updates, feature enhancements, and potential API or UI changes in upcoming versions.

------------------------------------------------------------
Features
------------------------------------------------------------
- AI-powered responses using OpenAI API
- Specialized for real estate queries and assistance
- Flask backend to handle requests
- Responsive UI with HTML, CSS, and JavaScript
- Secure API key storage with .env
- Easy to customize and extend

------------------------------------------------------------
Project Folder Structure
------------------------------------------------------------

- `app.py`: Flask backend logic
- `templates/`
  - `index.html`: Frontend HTML files (chat interface)
- `static/`: Static assets for styling and interactivity
  - `style.css`: Chat UI styles
  - `script.js`: Client-side JavaScript logic
- `.gitignore`: Excludes sensitive files and unnecessary cache from Git tracking
- `.env`: Environment variables (API key configuration, excluded from GitHub)
- `README.md`: Project documentation

------------------------------------------------------------
Installation & Setup
------------------------------------------------------------
1. Clone the repository
- git clone https://github.com/your-username/your-repo-name.git
- cd your-repo-name

2. Create a virtual environment:
- python -m venv venv
- source venv/bin/activate       # Mac/Linux
- venv\Scripts\activate          # Windows

3. Install dependencies:
- pip install flask python-dotenv openai

4. Create a .env file and add your API key:
- OPENAI_API_KEY=your_api_key_here

5. Run the app:
- python app.py

6. Open your browser at:
   http://127.0.0.1:5000/

------------------------------------------------------------
Future Improvements and Developments
------------------------------------------------------------
- Multi-session conversation support
- Save chat history
- Dark mode
- Integration with live real estate databases/APIs
- Automated appointment scheduling via calendar API integration
- Advanced property search & filtering with dynamic parameters (location, price, property type, etc.)
- Real-time market data integration from external APIs for live pricing trends and analytics
- Web deployment

