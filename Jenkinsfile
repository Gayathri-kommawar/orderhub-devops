pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out OrderHub source code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t orderhub:latest .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                bat 'docker images orderhub'
            }
        }
    }

    post {
        success {
            echo 'OrderHub CI pipeline completed successfully!'
        }

        failure {
            echo 'OrderHub CI pipeline failed. Check the Console Output.'
        }
    }
}
