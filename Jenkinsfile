pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                bat '''
                if not exist venv (
                    python -m venv venv
                )
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                cd "Test Automation/Amazon - jenkins"
                ..\\..\\venv\\Scripts\\pytest --junitxml=..\\..\\results.xml
                """
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
    }
}
