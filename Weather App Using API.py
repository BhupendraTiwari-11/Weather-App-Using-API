import tkinter as tk
from tkinter import messagebox

# Mock weather data for Indian cities (simulating API response)
weather_data = {
    "Delhi": {"temp": 32, "description": "Sunny", "humidity": 60},
    "Mumbai": {"temp": 29, "description": "Humid", "humidity": 85},
    "Chennai": {"temp": 34, "description": "Hot", "humidity": 70},
    "Kolkata": {"temp": 31, "description": "Cloudy", "humidity": 75},
    "Bangalore": {"temp": 26, "description": "Pleasant", "humidity": 65},
    "Hyderabad": {"temp": 30, "description": "Warm", "humidity": 68},
    "Ahmedabad": {"temp": 33, "description": "Sunny", "humidity": 55},
    "Pune": {"temp": 28, "description": "Pleasant", "humidity": 62},
    "Jaipur": {"temp": 35, "description": "Hot", "humidity": 50},
    "Lucknow": {"temp": 31, "description": "Cloudy", "humidity": 72},
    "Kanpur": {"temp": 32, "description": "Sunny", "humidity": 65},
    "Nagpur": {"temp": 30, "description": "Warm", "humidity": 70},
    "Indore": {"temp": 29, "description": "Pleasant", "humidity": 60},
    "Bhopal": {"temp": 28, "description": "Cloudy", "humidity": 68},
    "Patna": {"temp": 33, "description": "Hot", "humidity": 74},
    "Vadodara": {"temp": 31, "description": "Sunny", "humidity": 58},
    "Coimbatore": {"temp": 27, "description": "Pleasant", "humidity": 66},
    "Kochi": {"temp": 28, "description": "Humid", "humidity": 80},
    "Agra": {"temp": 34, "description": "Hot", "humidity": 52},
    "Surat": {"temp": 30, "description": "Warm", "humidity": 78},
    "Bhubaneswar": {"temp": 29, "description": "Cloudy", "humidity": 76},
    "Jamshedpur": {"temp": 30, "description": "Warm", "humidity": 70},
    "Gurugram": {"temp": 32, "description": "Sunny", "humidity": 58},
    "Noida": {"temp": 31, "description": "Sunny", "humidity": 60},
    "Navi Mumbai": {"temp": 29, "description": "Humid", "humidity": 82},
    "Trivandrum": {"temp": 27, "description": "Pleasant", "humidity": 79},
    "Vizag": {"temp": 30, "description": "Humid", "humidity": 77},
    "Dehradun": {"temp": 25, "description": "Cool", "humidity": 64},
    "Guwahati": {"temp": 29, "description": "Cloudy", "humidity": 80}
}

def get_weather():
    city = city_entry.get().capitalize()
    if city in weather_data:
        temp = weather_data[city]["temp"]
        desc = weather_data[city]["description"]
        hum = weather_data[city]["humidity"]
        
        # Update labels with weather info
        result_label.config(text=f"Temperature: {temp}°C\nDescription: {desc}\nHumidity: {hum}%")
        
        # Simulate weather icon with text (e.g., Sunny -> ☀️)
        icon = "☀️" if desc in ["Sunny", "Hot"] else "☁️" if desc == "Cloudy" else "💧" if desc in ["Humid", "Warm"] else "❄️"
        icon_label.config(text=icon, font=("Arial", 40))
    else:
        messagebox.showerror("Error", "City not found! Please enter a valid Indian city.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x400")
root.configure(bg="#E6F0FA")  # Light blue background for the window

# Add widgets with background and foreground colors for contrast
city_label = tk.Label(root, text="Enter Indian City:", font=("Arial", 12), bg="#E6F0FA", fg="#333333")
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF", fg="#333333")
city_entry.pack(pady=10)

get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#4A90E2", fg="#FFFFFF")
get_button.pack(pady=10)

icon_label = tk.Label(root, text="🌍", font=("Arial", 40), bg="#E6F0FA", fg="#333333")
icon_label.pack(pady=10)

result_label = tk.Label(root, text="Weather will appear here", font=("Arial", 12), justify="center", bg="#E6F0FA", fg="#333333")
result_label.pack(pady=10)

# Start the app
root.mainloop()
