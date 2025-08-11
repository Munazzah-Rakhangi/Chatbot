from flask import Flask, render_template, request, jsonify, session
import json
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session storage

# Load static Q&A from data.json
with open("data.json") as f:
    qa_pairs = json.load(f)

# Function to clean AI output and ensure pure HTML
def markdown_to_html(text):
    # Convert **bold** to <strong>
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    # Convert *italic* to <em> if needed
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    # Wrap in <p> if no HTML tags detected
    if not re.search(r"<.*?>", text):
        text = f"<p>{text}</p>"
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Retrieve conversation history from session
    conversation = session.get("conversation", [])

    # Check if the message matches predefined Q&A
    for qa in qa_pairs:
        if qa["question"] in user_message:
            bot_reply = qa["answer"]
            bot_reply = markdown_to_html(bot_reply)  # Ensure HTML output
            conversation.append({"role": "user", "content": user_message})
            conversation.append({"role": "assistant", "content": bot_reply})
            session["conversation"] = conversation
            return jsonify({"reply": bot_reply})

    # Add user message to history
    conversation.append({"role": "user", "content": user_message})

    # Prepare messages for AI
    messages = [
        {
            "role": "system",
            "content": """
You are a helpful real estate assistant.
Always reply in pure HTML — never use Markdown.
Wrap your entire message in valid HTML tags.
Use <p> for paragraphs, <strong> for bold text, and <ul><li> for bullet points.
Never output ** or * for bold — always use <strong>.
Example:
<p>Got it! Let's start with the details for renting a house.</p>
<ul>
    <li><strong>First question:</strong> What location or area are you considering for your rental?</li>
</ul>
"""
        }
    ] + conversation

    # Get AI response
    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150
    )

    bot_reply = ai_response.choices[0].message.content
    bot_reply = markdown_to_html(bot_reply)  # Ensure HTML output

    # Save bot reply to conversation
    conversation.append({"role": "assistant", "content": bot_reply})
    session["conversation"] = conversation

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
