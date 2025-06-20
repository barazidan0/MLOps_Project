pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mlops-image"
        CONTAINER_NAME = "mlops-container"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/barazidan0/MLOps_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t %DOCKER_IMAGE% ."
                }
            }
        }

        stage('Test & MLflow Logging') {
            steps {
                script {
                    bat "docker run --rm -v %cd%:/app -w /app %DOCKER_IMAGE% python eda_of_netflix_dataset.py"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat "docker stop %CONTAINER_NAME% || exit 0"
                    bat "docker rm %CONTAINER_NAME% || exit 0"
                    bat "docker run -d --name %CONTAINER_NAME% -p 5000:5000 %DOCKER_IMAGE%"
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
