# Welcome to the Weather Data Collector Project!

Thank you for visiting this repository! 🎉

This project is a Python application designed to fetch weather data from the OpenWeather API and store it in a MySQL database. Created for Docker practice, it demonstrates the power of containerization and how to work with APIs and databases seamlessly.

Whether you're here to learn, contribute, or simply explore, we hope you find this project insightful and enjoyable. Feel free to dive into the code, open issues, and submit pull requests. Your feedback and contributions are greatly appreciated!

Happy coding! 😊

---

## Quick Links

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

```markdown
# Weather Data Collector

This project is a Python application that collects weather data from the OpenWeather API and stores it in a MySQL database. It is designed for Docker practice and demonstrates how to use Docker to containerize a Python application.

## Features

- Fetch weather data from OpenWeather API
- Store weather data in a MySQL database
- Dockerized application for easy deployment

## Prerequisites

- Docker
- Docker Compose
- OpenWeather API Key

## Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/weather-data-collector.git
cd weather-data-collector
```

### Setup environment variables

Create a `.env` file in the root directory and add your OpenWeather API key:

```dotenv
OPENWEATHER_API_KEY=your_api_key
MYSQL_ROOT_PASSWORD=your_mysql_root_password
MYSQL_DATABASE=weather_db
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_user_password
```

### Build Docker Image

```bash
docker build -t weather-data-collector .
```

### Run Docker Container

```bash
docker run --name weather-container --env-file .env -d weather-data-collector
```

### Access MySQL Database

To access the MySQL database running inside the container, use the following command:

```bash
docker exec -it mysql-container mysql -u root -p
```

Enter the root password from your `.env` file.

## Usage

To run the application, use the following command:

```bash
docker exec -it weather-container python main.py
```

## Contributing

Feel free to open issues or submit pull requests if you want to contribute to this project.


## Acknowledgements

- [OpenWeather](https://openweathermap.org/) for their awesome API
- [Docker](https://www.docker.com/) for containerization

```

Feel free to modify this `README.md` to fit your project details and preferences. If you need any further customization or additional sections, just let me know! Happy coding! 😊
