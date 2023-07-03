import tkinter as tk
import requests
from PIL import Image, ImageTk

def get_weather():
    city = city_entry.get()
    api_key = '164fe144a41ec5f0c8fb1e9930ab33ee'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        icon_id = weather_data['weather'][0]['icon']

        weather_label['text'] = f'Temperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'

        # Display weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        icon_response = requests.get(icon_url, stream=True)
        if icon_response.status_code == 200:
            icon_image = Image.open(icon_response.raw)
            icon_image = icon_image.resize((100, 100), Image.ANTIALIAS)
            weather_icon = ImageTk.PhotoImage(icon_image)
            icon_label.configure(image=weather_icon)
            icon_label.image = weather_icon
    else:
        weather_label['text'] = 'Failed to fetch weather data.'
        icon_label.configure(image='')

# Create the main window
window = tk.Tk()
window.title('WeatherME')
window.configure(bg='#f5f5f5')

# Create and pack the widgets
title_label = tk.Label(window, text='WeatherME', font=('Arial', 20), bg='#f5f5f5')
title_label.pack(pady=10)

city_frame = tk.Frame(window, bg='#f5f5f5')
city_frame.pack()

city_label = tk.Label(city_frame, text='Enter a city:', font=('Arial', 12), bg='#f5f5f5')
city_label.pack(side='left')

city_entry = tk.Entry(city_frame, font=('Arial', 12), bd=1, relief='solid')
city_entry.pack(side='left')

submit_button = tk.Button(window, text='Get Weather', font=('Arial', 12), relief='raised', command=get_weather)
submit_button.pack(pady=10)

weather_icon_frame = tk.Frame(window, bg='#f5f5f5')
weather_icon_frame.pack()

icon_label = tk.Label(weather_icon_frame, bg='#f5f5f5')
icon_label.pack(side='left')

weather_label = tk.Label(window, text='', font=('Arial', 12), bg='#f5f5f5', justify='left')
weather_label.pack()

# Start the main event loop
window.mainloop()
