import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Add graph_module path
sys.path.append(os.path.abspath("../../"))
import sys
import os
sys.path.append(os.path.abspath("../"))  # adds parent folder to path
from graph import show_graphs


# --- Step 1: Load Knowledge Base ---
with open("knowledge_base.txt", "r") as f:
  knowledge = f.read().splitlines()

vectorizer = TfidfVectorizer()
kb_vectors = vectorizer.fit_transform(knowledge)


data = pd.read_csv("campus_data.csv")


months = np.array(range(len(data))).reshape(-1,1)
electricity = data["Electricity"].values
water = data["Water"].values
waste = data["Waste"].values

model_elec = LinearRegression().fit(months, electricity)
model_water = LinearRegression().fit(months, water)
model_waste = LinearRegression().fit(months, waste)

next_month = np.array([[len(data)]])
pred_elec = int(model_elec.predict(next_month)[0])
pred_water = int(model_water.predict(next_month)[0])
pred_waste = int(model_waste.predict(next_month)[0])

# --- Step 3: Recommendation Engine ---
def recommend(elec, water, waste):
    recs = []
    if elec > 14000:
        recs.append("Reduce AC and lights usage; use energy-efficient devices.")
    if water > 500000:
        recs.append("Implement rainwater harvesting and fix water leaks.")
    if waste > 3800:
        recs.append("Improve waste segregation and recycling awareness.")
    return recs

recs = recommend(pred_elec, pred_water, pred_waste)

# --- Step 4: Chatbot Response ---
def get_response(question):
    q_lower = question.lower()

    # Line graph
    if "graph" in q_lower:
        return "📊 Graph generated!"

    # Pie chart
    if "pie" in q_lower:
        return " Pie chart generated!"

    # Predictions
    if "electricity" in q_lower and "predict" in q_lower:
        return f"🔮 Predicted next month electricity usage: {pred_elec} kWh"

    if "water" in q_lower and "predict" in q_lower:
        return f"🔮 Predicted next month water usage: {pred_water} Litres"

    if "waste" in q_lower and "predict" in q_lower:
        return f"🔮 Predicted next month waste: {pred_waste} kg"

    # Advice
    if "advice" in q_lower or "recommend" in q_lower:
        return "💡 Recommendations:\n- " + "\n- ".join(recs)

    # Knowledge base fallback
    q_vec = vectorizer.transform([question])
    sim = cosine_similarity(q_vec, kb_vectors)
    index = sim.argmax()
    return knowledge[index]
    if "." in full_sentence:
        first_sentence = full_sentence.split(".")[0] + "."
    else:
        first_sentence = full_sentence
    return first_sentence


import matplotlib.pyplot as plt
import pandas as pd
import os

def create_graphs():
    data = pd.read_csv("campus_data.csv")

    months = range(len(data))

    plt.figure(figsize=(8,5))
    plt.plot(months, data['Electricity'], marker='o', label='Electricity (kWh)')
    plt.plot(months, data['Water'], marker='s', label='Water (L)')
    plt.plot(months, data['Waste'], marker='^', label='Waste (kg)')
    plt.xlabel("Months")
    plt.ylabel("Usage")
    plt.title("Campus Resource Usage")
    plt.legend()
    # Save the figure to static folder
    img_path = os.path.join(os.path.dirname(__file__), "static", "graphs.png")
    plt.savefig(img_path)
    plt.close()
    return "/static/graphs.png"  # Path for HTML

def show_pie_chart():
    import matplotlib.pyplot as plt
    import pandas as pd
    import os

    data_path = os.path.join(os.path.dirname(__file__), "campus_data.csv")
    data = pd.read_csv(data_path)

    totals = [
        data["Electricity"].sum(),
        data["Water"].sum(),
        data["Waste"].sum()
    ]

    labels = ["Electricity", "Water", "Waste"]

    plt.figure(figsize=(6,6))
    plt.pie(totals, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Campus Resource Distribution")

    static_path = os.path.join(os.path.dirname(__file__), "static", "pie.png")
    plt.savefig(static_path)
    plt.close()

    return "/static/pie.png"

