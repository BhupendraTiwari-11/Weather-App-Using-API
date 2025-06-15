import tkinter as tk
from tkinter import messagebox

# Mock weather data (simulating API response due to Pyodide restrictions)
mock_weather_data = {
    "london": {"temp": 15, "description": "Cloudy", "humidity": 80},
    "paris": {"temp": 18, "description": "Sunny", "humidity": 65},
    "new york": {"temp": 22, "description": "Rainy", "humidity": 70}
}

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")
        self.root.configure(bg="#b3e5fc")  # Light blue background

        # Title label
        self.title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"), bg="#b3e5fc")
        self.title_label.pack(pady=10)

        # City input
        self.city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg="#b3e5fc")
        self.city_label.pack(pady=5)
        self.city_entry = tk.Entry(root, font=("Arial", 12))
        self.city_entry.pack(pady=5)

        # Fetch button
        self.fetch_button = tk.Button(root, text="Get Weather", command=self.get_weather, bg="#4fc3f7")
        self.fetch_button.pack(pady=10)

        # Weather display labels
        self.temp_label = tk.Label(root, text="", font=("Arial", 12), bg="#b3e5fc")
        self.temp_label.pack(pady=5)
        self.desc_label = tk.Label(root, text="", font=("Arial", 12), bg="#b3e5fc")
        self.desc_label.pack(pady=5)
        self.humidity_label = tk.Label(root, text="", font=("Arial", 12), bg="#b3e5fc")
        self.humidity_label.pack(pady=5)

    def get_weather(self):
        city = self.city_entry.get().strip().lower()
        if not city:
            messagebox.showerror("Error", "Please enter a city name!")
            return

        # Fetch mock weather data
        if city in mock_weather_data:
            weather = mock_weather_data[city]
            self.temp_label.config(text=f"Temperature: {weather['temp']}°C")
            self.desc_label.config(text=f"Description: {weather['description']}")
            self.humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        else:
            messagebox.showerror("Error", f"City '{city}' not found!")
            self.temp_label.config(text="")
            self.desc_label.config(text="")
            self.humidity_label.config(text="")

# Run the app
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
