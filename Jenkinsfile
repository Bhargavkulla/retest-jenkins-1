pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Generate Coverage Report') {
            steps {
                sh '''
                    coverage run -m pytest
                    coverage report
                    coverage html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
        }
    }
}
