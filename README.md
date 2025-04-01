# 🌦️ Weather by Photo – Telegram Bot Documentation

## 🤖 Bot Name
**Weather by Photo Bot**

## 📝 Description
This Telegram bot allows users to receive real-time weather updates by simply sending a **photo of a city**. The bot analyzes the photo to determine the **city/location** and returns the current weather. Users can also request **random city weather** without sending a photo.

---

## 🚀 Features

- 📸 Send a photo of a city → Get current weather for that city
- 🎲 Request weather from a random city
- 🌍 Supports global cities
- ☁️ Weather info includes:
  - Temperature
  - Weather condition (e.g., sunny, cloudy, rainy)
  - Humidity
  - Wind speed

---

## 🧠 How It Works

1. **Photo Input**:
   - The user sends a **photo** of a city to the bot.
   - The bot uses an **image recognition API** to detect the location.
   - The detected city name is used to query a **weather API**.
   - The bot sends back the weather details.

---

## 🔧 Commands

| Command      | Description                          |
|--------------|--------------------------------------|
| `/start`     | Starts the bot and shows help menu   |     |

---

## 🖼️ Example Usage

### 1. Sending a Photo
- User sends a photo of **New York City**.
- Bot replies:
📍 New York City 🌤️ Condition: Partly Cloudy 🌡️ Temp: 22°C 💧 Humidity: 55% 🌬️ Wind: 13 km/h

markdown
Copy
Edit

### 2. Random City
- User sends `/random`.
- Bot replies:
📍 Tokyo 🌧️ Condition: Light Rain 🌡️ Temp: 17°C 💧 Humidity: 78% 🌬️ Wind: 20 km/h

yaml
Copy
Edit

---

## ⚙️ Technologies Used

- **Telegram Bot API** – for messaging
- **Image Recognition API** – to detect location from photo
- **Weather API** (e.g., OpenWeatherMap) – for real-time weather
- **Python / Node.js** – backend logic

---

## 📌 Notes

- The bot performs best with **landmark photos** or **clear city views**.
- Weather data might vary slightly depending on the detected location accuracy.

---

## 🧑‍💻 Developer

**Created by:** [Daniil Lapushkin]  
**GitHub:** [Baton111]  
**Telegram:** [@kef4rchik]

---


