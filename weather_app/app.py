import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Weather

API_KEY = 'your-api-key'
CITY = 'Indore'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

def fetch_weather_data():
    response = requests.get(URL)
    data = response.json()
    return data

def main():
    engine = create_engine('mysql+mysqlconnector://your-sql-user:your-sql-passwd@your-database-IP or localhost/weather_db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    weather_data = fetch_weather_data()
    weather = Weather(
        city=weather_data['name'],
        temperature=weather_data['main']['temp'],
        description=weather_data['weather'][0]['description']
    )
    
    session.add(weather)
    session.commit()

if __name__ == "__main__":
    main()

