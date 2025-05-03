pipeline {
    agent {
        docker {
            image 'python:3.10'  // You can also use python:3.11
        }
    }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Pradhisha-N/retest-jenkins-1.git', branch: 'main'
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                    python -m venv $VENV
                    $VENV/bin/pip install --upgrade pip
                    $VENV/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    $VENV/bin/python -m pytest
                '''
            }
        }

        stage('Coverage Report') {
            steps {
                sh '''
                    $VENV/bin/coverage run -m pytest
                    $VENV/bin/coverage report
                    $VENV/bin/coverage html
                '''
                publishHTML(target: [
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }

    post {
        always {
            sh 'rm -rf $VENV'
        }
    }
}
