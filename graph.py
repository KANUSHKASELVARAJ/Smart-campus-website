# graph.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to create line/bar graphs
def show_graphs():
    # Path to CSV
    data_path = os.path.join(os.path.dirname(__file__), "campus_data.csv")
    data = pd.read_csv(data_path)
    
    fig, axs = plt.subplots(3,1,figsize=(12,14), facecolor="#f5f5f5")
    
    # Electricity Line Graph
    axs[0].plot(data["Month"], data["Electricity"], marker='o', color='orange', linewidth=3)
    axs[0].set_title("Monthly Electricity Consumption (kWh)", fontsize=14, fontweight='bold')
    axs[0].set_ylabel("Electricity (kWh)")
    axs[0].grid(True, linestyle='--', alpha=0.7)
    
    # Water Line Graph
    axs[1].plot(data["Month"], data["Water"], marker='s', color='blue', linewidth=3)
    axs[1].set_title("Monthly Water Consumption (Litres)", fontsize=14, fontweight='bold')
    axs[1].set_ylabel("Water (Litres)")
    axs[1].grid(True, linestyle='--', alpha=0.7)
    
    # Waste Bar Graph
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
    axs[2].bar(data["Month"], data["Waste"], color=colors, edgecolor='black', linewidth=1.2)
    axs[2].set_title("Monthly Waste Generation (kg)", fontsize=14, fontweight='bold')
    axs[2].set_xlabel("Month")
    axs[2].set_ylabel("Waste (kg)")
    axs[2].grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout(pad=3.0)
    
    # Save image to static folder
    static_path = os.path.join(os.path.dirname(__file__), "static", "graphs.png")
    plt.savefig(static_path)
    plt.close()
    
    return "/static/graphs.png"  # path for HTML to display

# Function to create pie chart
def show_pie_chart():
    data_path = os.path.join(os.path.dirname(__file__), "campus_data.csv")
    data = pd.read_csv(data_path)

    totals = [
        data["Electricity"].sum(),
        data["Water"].sum(),
        data["Waste"].sum()
    ]
    labels = ["Electricity", "Water", "Waste"]

    plt.figure(figsize=(6,6))
    plt.pie(totals, labels=labels, autopct="%1.1f%%", startangle=140, colors=['orange','blue','green'])
    plt.title("Campus Resource Distribution")
    
    static_path = os.path.join(os.path.dirname(__file__), "static", "pie.png")
    plt.savefig(static_path)
    plt.close()
    
    return "/static/pie.png"  # path for HTML to display
