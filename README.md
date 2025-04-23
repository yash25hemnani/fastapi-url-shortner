
# FastAPI URL Shortener

# 🔗 FastAPI URL Shortener

A simple and efficient URL shortener built using **FastAPI**, **PostgreSQL**, and **Docker**. This project allows you to shorten long URLs and access them via a generated short code.

## 🚀 Features

- Shortens long URLs to short, shareable links
- FastAPI-based backend for performance and ease of development
- PostgreSQL as the database to store original and shortened URLs
- Dockerized for easy deployment

## 🛠️ Tech Stack

- **Python 3.12**
- **FastAPI**
- **PostgreSQL**
- **Docker**
- **Uvicorn**

## 📦 Installation & Setup

### Prerequisites

- Docker & Docker Compose
- Python 3.12 (for local development)

## Run the Project Using Docker
To run the project using Docker, follow these steps:

1. Pull the image from Docker Hub:
   ```
   docker pull yash2522hemnani/fastapi-url-shortener
   ```

2. Run the container:
   ```
   docker run -d -p 8000:8000 yash2522hemnani/fastapi-url-shortener
   ```

Once the container is up and running, you can access the URL shortener at `http://0.0.0.0:8000`.

## Local Installation (Using FastAPI Structure)
To install and run the project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourgithubusername/fastapi-url-shortener.git
   cd fastapi-url-shortener
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scriptsctivate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the FastAPI app using `uvicorn`:
   ```
   uvicorn app.main:app --reload
   ```

The app will be available at `http://127.0.0.1:8000`.

## Database Configuration
No need to connect to a local database. The database is hosted online using **Aiven**.

## 🧪 API Endpoints

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| GET    | `/`            | Welcome message         |
| POST   | `/shorten`     | Shorten a given URL     |
| GET    | `/{short_url}` | Redirect to original URL|

### Sample Request

```http
POST /shorten
Content-Type: application/json

{
  "original_url": "https://www.example.com"
}
```

## 🧾 Example `.env` (if you want to connect your own aiven database)

```
DATABASE_URL=postgresql://user:password@host:port/dbname
```


Enjoy using the FastAPI URL Shortener!
