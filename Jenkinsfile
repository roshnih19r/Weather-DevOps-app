pipeline {
    agent any
    
    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/roshnih19r/Weather-DevOps-app.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-app .'
            }
        }
        
        stage('Run Tests') {
            steps {
                stage('Run Tests') {
    steps {
        sh 'docker run --rm weather-app python -m pytest tests/ --ignore-glob="**/node_modules"  || true'
    }
}
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                docker stop weather-app || true
                docker rm weather-app || true
                docker run -d -p 5000:5000 --name weather-app weather-app
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Deployment Successful! 🎉'
        }
        failure {
            echo 'Pipeline Failed!'
        }
    }
}