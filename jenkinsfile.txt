pipeline {
    agent any
    environment {
        IMAGE_NAME = "swaralil22/terminal-app"
        CREDENTIALS_ID = "dockerhub-credentials" 
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build & Test') {
            steps {
                echo "Running syntax check for terminal application..."
                sh "python -m py_compile app.py"
            }
        }
        stage('Docker Build & Push') {
            steps {
                script {
                    app = docker.build("${env.IMAGE_NAME}:${env.BUILD_NUMBER}")
                    docker.withRegistry('https://index.docker.io/v1/', "${env.CREDENTIALS_ID}") {
                        app.push("latest")
                        app.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                sh "kubectl apply -f k8s/deployment.yaml"
                sh "kubectl apply -f k8s/service.yaml"
            }
        }
    }
}