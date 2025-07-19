pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/HARSHITHA-G-M/FlaskOps-cicd.git'
            }
        }
        stage('Setup Python Virtual Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                cd app
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python -m unittest discover -s app -p "test_app.py"
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
}
