pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                bat """
                python -m venv venv
                venv\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat "venv\\Scripts\\pytest --junitxml=results.xml"
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}
