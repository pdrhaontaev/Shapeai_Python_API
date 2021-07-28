import tkinter as tk
import requests
from datetime import datetime


def getweather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=d9a0501776cf73e1aa2140fd7311887f"

    api_data = requests.get(api).json()
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    final_info = str(weather_desc) + "\n" + "Temperature:" + str(temp_city) + "°C"
    final_data = "\n" + "Date_Time: " + str(date_time) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind_spd)
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getweather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
