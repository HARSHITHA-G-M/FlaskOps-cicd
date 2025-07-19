# FlaskOps CI/CD Project 🚀

A simple **Flask Web Application** integrated with a **Jenkins CI/CD pipeline** and containerized using **Docker**.  
The project demonstrates how to automate testing, building, and deployment of a Python web app.

---

## 📌 **Features**

✅ REST API with multiple endpoints  
✅ Automated CI/CD using Jenkins Pipeline  
✅ Unit tests for API endpoints  
✅ Dockerized Flask app  
✅ Automatic deployment after successful build  

---

## 🗂 **Project Structure**

├── app/app.py # Main Flask application
├── app/requirements.txt # Python dependencies
├── test/
│ └── test_app.py # Unit tests for the Flask app
├── Dockerfile # Docker image configuration
├── Jenkinsfile # Jenkins Pipeline script
└── README.md # Project documentation


---

## ⚡ **API Endpoints**

| Method | Endpoint          | Description                                      | Example |
|--------|--------------------|--------------------------------------------------|---------|
| GET    | `/`               | Home route – Welcome message                      | `http://localhost:5000/` |
| GET    | `/health`         | Health check – returns service status             | `http://localhost:5000/health` |
| GET    | `/add?a=5&b=10`   | Addition of two numbers (query params)            | `http://localhost:5000/add?a=5&b=10` |
| GET    | `/subtract?a=20&b=5` | Subtraction of two numbers (query params)      | `http://localhost:5000/subtract?a=20&b=5` |
| POST   | `/multiply`       | Multiplication (JSON body: `{ "a": 5, "b": 6 }`)  | `curl -X POST http://localhost:5000/multiply -H "Content-Type: application/json" -d '{"a":5,"b":6}'` |
| POST   | `/divide`         | Division (JSON body: `{ "a": 10, "b": 2 }`)       | `curl -X POST http://localhost:5000/divide -H "Content-Type: application/json" -d '{"a":10,"b":2}'` |

---

## 🐳 **Run with Docker**

1. Build the image**
docker build -t flask-app .

2 Run the container
docker run -d -p 5000:5000 flask-app

3. Access the App
Open in your browser:
Home: http://localhost:5000
Health check: http://localhost:5000/health


⚙️ CI/CD Pipeline (Jenkins)
The pipeline (Jenkinsfile) performs:
Checkout Code – Pulls latest code from GitHub
Setup Python Virtual Environment – Installs dependencies from requirements.txt
Run Unit Tests – Executes test_app.py
Build Docker Image – Builds the Flask app as a Docker image
Deploy – Runs the container automatically if all stages pass

📬 Contributing
Feel free to fork this repo, submit issues, or open pull requests to improve the project.


🖥 Author
👩‍💻 Developed by [HARSHITHA-G-M]
📌 CI/CD with Jenkins + Docker + Python Flask

