pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/HARSHITHA-G-M/FlaskOps-cicd.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t flask-app .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed! Check errors above.'
        }
    }
}

