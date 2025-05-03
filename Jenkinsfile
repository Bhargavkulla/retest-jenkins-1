pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Check Python') {
            steps {
                sh '''
                    which python3
                    python3 --version
                    which pip3
                    pip3 --version
                    pip3 show pytest
                '''
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
