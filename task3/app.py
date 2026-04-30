from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize
from difflib import get_close_matches
from datetime import datetime

app = Flask(__name__)

# ---------------- TOKENIZER SETUP ----------------
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

# ---------------- BASIC Q&A ----------------
qa_data = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "how are you": "I am fine, thanks!",
    "what is python": "Python is a versatile programming language widely used in AI, web development, and automation.",
    "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence by machines, enabling learning and decision-making.",
    "what is dbms": "DBMS (Database Management System) is software that stores, organizes, and manages data efficiently.",
    "what is sql": "SQL (Structured Query Language) is used to query and manage data in relational databases.",
    "what is oops": "OOP (Object-Oriented Programming) is a paradigm based on objects, classes, inheritance, and encapsulation.",
    "what is ml": "Machine Learning is a subset of AI that enables systems to learn patterns from data and improve over time.",
    "what is deep learning": "Deep Learning is a branch of ML that uses neural networks with multiple layers to model complex patterns.",
    "what is cloud computing": "Cloud computing delivers computing services like storage, databases, and servers over the internet on demand.",
    "what is data science": "Data Science combines statistics, programming, and domain knowledge to extract insights from data."
}

# ---------------- COUNTRY & STATE DATA ----------------
geo_data = {
    "india": "India is a country in South Asia. Capital: New Delhi.",
    "usa": "USA is a country in North America. Capital: Washington D.C.",
    "japan": "Japan is an island country in East Asia. Capital: Tokyo.",
    "china": "China is a country in East Asia. Capital: Beijing.",

    "andhra pradesh": "Andhra Pradesh is a state in India. Capital: Amaravati.",
    "telangana": "Telangana is a state in India. Capital: Hyderabad.",
    "tamil nadu": "Tamil Nadu is a state in India. Capital: Chennai.",
    "karnataka": "Karnataka is a state in India. Capital: Bengaluru.",
    "kerala": "Kerala is a state in India. Capital: Thiruvananthapuram."
}

# ---------------- ROADMAP SYSTEM ----------------
roadmap = {
    "first year": {
        "web": "1st Year Web Dev: Learn HTML, CSS, basic JavaScript, build static websites.",
        "ai": "1st Year AI: Focus on Python basics, logic building, and math fundamentals.",
        "default": "1st Year: Learn C/Python, basics of programming, and problem solving."
    },
    "second year": {
        "web": "2nd Year Web Dev: Learn JavaScript deeply, React, APIs, build projects.",
        "ai": "2nd Year AI: Learn NumPy, Pandas, and basics of Machine Learning.",
        "default": "2nd Year: Focus on DSA, DBMS, OOP, and mini projects."
    },
    "third year": {
        "web": "3rd Year Web Dev: Learn full-stack (MERN/MEAN), advanced projects.",
        "ai": "3rd Year AI: Learn Machine Learning, Deep Learning, AI projects.",
        "default": "3rd Year: Focus on internships, advanced DSA, real-world projects."
    },
    "fourth year": {
        "web": "4th Year Web Dev: Master full-stack, deployment, system design basics.",
        "ai": "4th Year AI: Work on AI final projects, research, optimization.",
        "default": "4th Year: Focus on placements, interviews, aptitude, resume building."
    }
}

# ---------------- SPAM WORDS ----------------
spam_words = ["win", "free", "offer", "money", "click"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get', methods=['POST'])
def chatbot():
    user_input = request.form['msg'].lower()
    words = word_tokenize(user_input)

    # ---------------- SPAM CHECK ----------------
    for word in words:
        if word in spam_words:
            return render_template("index.html", reply="⚠ This message appears to be spam and cannot be processed.")

    # ---------------- GREETING (TIME BASED) ----------------
    current_hour = datetime.now().hour
    if any(greet in words for greet in ["hi", "hello", "hey"]):
        if 5 <= current_hour < 12:
            return render_template("index.html", reply="🌅 Good morning! How may I assist you today?")
        elif 12 <= current_hour < 17:
            return render_template("index.html", reply="🌞 Good afternoon! How may I assist you today?")
        elif 17 <= current_hour < 21:
            return render_template("index.html", reply="🌙 Good evening! How may I assist you today?")
        else:
            return render_template("index.html", reply="🌃 Good night! How may I assist you today?")

    # ---------------- HEALTH ----------------
    if "fever" in words:
        return render_template("index.html", reply="Please take rest and stay hydrated.")
    elif "cold" in words:
        return render_template("index.html", reply="Stay warm and drink hot fluids.")
    elif "headache" in words:
        return render_template("index.html", reply="Take rest and avoid screen exposure.")

    # ---------------- COUNTRY / STATE INFO ----------------
    for key in geo_data:
        if key in user_input:
            return render_template("index.html", reply=geo_data[key])

    # ---------------- ROADMAP SYSTEM ----------------
    if "year" in user_input:
        for year in roadmap:
            if year in user_input:
                if "web" in user_input:
                    return render_template("index.html", reply=roadmap[year]["web"])
                elif "ai" in user_input:
                    return render_template("index.html", reply=roadmap[year]["ai"])
                else:
                    return render_template("index.html", reply=roadmap[year]["default"])

    # ---------------- AI / ML ----------------
    if ("ai" in words or "artificial intelligence" in user_input) and "difference" not in user_input:
        reply = """
        <b>AI / ML Path:</b>
        <ul>
        <li>Learn Python programming</li>
        <li>Strengthen Mathematics basics</li>
        <li>Study Machine Learning algorithms</li>
        </ul>
        """
        return render_template("index.html", reply=reply)

    # ---------------- MATH ----------------
    try:
        result = eval(user_input)
        return render_template("index.html", reply="Answer: " + str(result))
    except:
        pass

    # ---------------- FUZZY MATCHING ----------------
    match = get_close_matches(user_input, qa_data.keys(), n=1)
    if match:
        reply = qa_data[match[0]]
    else:
        # ---------------- FORMAL FALLBACK ----------------
        reply = """
        🤖 I sincerely apologize, but I am unable to provide an appropriate answer for your query.  
        Please rephrase your question or ask something related to programming, AI, web development, or general knowledge.
        """

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
