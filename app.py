from flask import Flask, render_template, request, jsonify
from smart_chatbot import get_response, create_graphs,show_pie_chart
import os
app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot endpoint
@app.route("/ask", methods=["POST"])
@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message").lower()

    if "pie" in user_input:
        pie_url = show_pie_chart()
        return jsonify({
            "response": "🥧 Pie chart generated!",
            "pie": pie_url
        })

    if "graph" in user_input:
        graph_url = create_graphs()
        return jsonify({
            "response": "📊 Graph generated!",
            "graph": graph_url
        })

    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    response = get_response(user_msg)

    return jsonify(response)

