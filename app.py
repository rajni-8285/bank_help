import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv



load_dotenv()
client = Groq(api_key="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") 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("script.html")

@app.route("/help")
def help_page():
    return render_template("index.html")
from flask import Flask, render_template, request, redirect, url_for, jsonify



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        return redirect(url_for('home')) 
    return render_template("login.html")



@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")


    chat_completion = client.chat.completions.create(
        messages=[{"role": "system", "content": "You are a professional customer help assistant for 'SecureBank'. Provide helpful, concise information about banking services, interest rates (Savings: 4%, FD: 7%), and account opening. If asked non-banking questions, politely decline."},
                {"role": "user", "content": user_message}],
        model="llama-3.3-70b-versatile",
    )

    ai_response = chat_completion.choices[0].message.content
    return jsonify({"reply": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
