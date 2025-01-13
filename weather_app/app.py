import time
import requests
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from database.models import Base, Weather

API_KEY = 'API-KEY'
CITY = 'Indore'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

def fetch_weather_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from OpenWeather API: {e}")
        return None

def main():
    try:
        engine = create_engine('mysql+mysqlconnector://db_user:db_passwd@localhost or IP/weather_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        while True:
            weather_data = fetch_weather_data()
            if weather_data:
                # Convert temperature from Kelvin to Celsius
                temperature_celsius = weather_data['main']['temp'] - 273.15 
                weather = Weather(
                    city=weather_data['name'],
                    temperature=temperature_celsius,
                    description=weather_data['weather'][0]['description']
                )

                session.add(weather)
                session.commit()
                print(f"Weather data for {CITY} stored in database: {temperature_celsius}°C")
            else:
                print("Failed to fetch weather data.")

            # Wait for 10 minutes before fetching data again
            time.sleep(600)

    except exc.SQLAlchemyError as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    main()

