pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/barazidan0/MLOps_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t mlops-image .'
                }
            }
        }

        stage('Run Pipeline Script') {
            steps {
                script {
                    sh 'docker run --rm mlops-image python eda_of_netflix_dataset.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker stop mlops-container || true'
                    sh 'docker rm mlops-container || true'
                    sh 'docker run -d --name mlops-container -p 5000:5000 mlops-image'
                }
            }
        }
    }

    post {
        failure {
            echo 'Build or Deploy failed. Please check logs.'
        }
    }
}
