import requests
import tkinter as tk

api_key = "YOUR_API_KEY"


def get_weather():
    city = entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data= response.json()
        print(data)

        if data.get("cod") != 200:
            result_text.set(f"Error: {data.get('message', 'City not found')}")
            return

        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        result_text.set(f"Temperature: {temp}\n\nHumidity: {desc}")
    except (KeyError,ValueError):
        result_text.set("temp not found")


# Tkinter Arayüzü
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter the city:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Show", command=get_weather, font=("Arial", 12)).pack(pady=10)



result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=350, justify="left", font=("Arial", 11)).pack(pady=20)

root.mainloop()

