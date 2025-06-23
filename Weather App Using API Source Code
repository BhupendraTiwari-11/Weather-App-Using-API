import tkinter as tk
from tkinter import messagebox

# Mock weather data for Indian cities (simulating API response)
weather_data = {
    "Delhi": {"temp": 32, "description": "Sunny", "humidity": 60, "aqi": "Moderate", "wind": 15},
    "Mumbai": {"temp": 29, "description": "Humid", "humidity": 85, "aqi": "Poor", "wind": 8},
    "Chennai": {"temp": 34, "description": "Hot", "humidity": 70, "aqi": "Unhealthy", "wind": 12},
    "Kolkata": {"temp": 31, "description": "Cloudy", "humidity": 75, "aqi": "Unhealthy", "wind": 10},
    "Bangalore": {"temp": 26, "description": "Pleasant", "humidity": 65, "aqi": "Good", "wind": 14},
    "Hyderabad": {"temp": 30, "description": "Warm", "humidity": 68, "aqi": "Moderate", "wind": 11},
    "Ahmedabad": {"temp": 33, "description": "Sunny", "humidity": 55, "aqi": "Moderate", "wind": 16},
    "Pune": {"temp": 28, "description": "Pleasant", "humidity": 62, "aqi": "Good", "wind": 13},
    "Jaipur": {"temp": 35, "description": "Hot", "humidity": 50, "aqi": "Moderate", "wind": 18},
    "Lucknow": {"temp": 31, "description": "Cloudy", "humidity": 72, "aqi": "Unhealthy", "wind": 9},
    "Kanpur": {"temp": 32, "description": "Sunny", "humidity": 65, "aqi": "Moderate", "wind": 15},
    "Nagpur": {"temp": 30, "description": "Warm", "humidity": 70, "aqi": "Moderate", "wind": 12},
    "Indore": {"temp": 29, "description": "Pleasant", "humidity": 60, "aqi": "Good", "wind": 14},
    "Bhopal": {"temp": 28, "description": "Cloudy", "humidity": 68, "aqi": "Moderate", "wind": 10},
    "Patna": {"temp": 33, "description": "Hot", "humidity": 74, "aqi": "Unhealthy", "wind": 11},
    "Vadodara": {"temp": 31, "description": "Sunny", "humidity": 58, "aqi": "Moderate", "wind": 15},
    "Coimbatore": {"temp": 27, "description": "Pleasant", "humidity": 66, "aqi": "Good", "wind": 13},
    "Kochi": {"temp": 28, "description": "Humid", "humidity": 80, "aqi": "Poor", "wind": 9},
    "Agra": {"temp": 34, "description": "Hot", "humidity": 52, "aqi": "Unhealthy", "wind": 16},
    "Surat": {"temp": 30, "description": "Warm", "humidity": 78, "aqi": "Moderate", "wind": 10},
    "Bhubaneswar": {"temp": 29, "description": "Cloudy", "humidity": 76, "aqi": "Unhealthy", "wind": 8},
    "Jamshedpur": {"temp": 30, "description": "Warm", "humidity": 70, "aqi": "Moderate", "wind": 11},
    "Gurugram": {"temp": 32, "description": "Sunny", "humidity": 58, "aqi": "Moderate", "wind": 14},
    "Noida": {"temp": 31, "description": "Sunny", "humidity": 60, "aqi": "Moderate", "wind": 15},
    "Navi Mumbai": {"temp": 29, "description": "Humid", "humidity": 82, "aqi": "Poor", "wind": 8},
    "Trivandrum": {"temp": 27, "description": "Pleasant", "humidity": 79, "aqi": "Good", "wind": 12},
    "Vizag": {"temp": 30, "description": "Humid", "humidity": 77, "aqi": "Poor", "wind": 9},
    "Dehradun": {"temp": 25, "description": "Cool", "humidity": 64, "aqi": "Good", "wind": 13},
    "Guwahati": {"temp": 29, "description": "Cloudy", "humidity": 80, "aqi": "Unhealthy", "wind": 7}
}

def get_weather():
    city = city_entry.get().capitalize()
    if city in weather_data:
        temp = weather_data[city]["temp"]
        desc = weather_data[city]["description"]
        hum = weather_data[city]["humidity"]
        aqi = weather_data[city]["aqi"]
        wind = weather_data[city]["wind"]
        
        # Update labels with weather info, including AQI and wind speed
        result_label.config(text=f"Temperature: {temp}°C\nDescription: {desc}\nHumidity: {hum}%\nAQI: {aqi}\nWind: {wind} km/h")
        
        # Simulate weather icon with text (e.g., Sunny -> ☀️)
        icon = "☀️" if desc in ["Sunny", "Hot"] else "☁️" if desc == "Cloudy" else "💧" if desc in ["Humid", "Warm"] else "❄️"
        icon_label.config(text=icon, font=("Arial", 40))
    else:
        messagebox.showerror("Error", "City not found! Please enter a valid Indian city.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x450")  # Slightly taller window to accommodate extra info
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
