pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Pradhisha-N/retest-jenkins-1.git', branch: 'main'
            }
        }
        stage('Install venv (Debian/Ubuntu)') {
            steps {
                sh '''
                    if ! python3 -m venv --help > /dev/null 2>&1; then
                        sudo apt update
                        sudo apt install -y python3.10-venv
                    fi
                '''
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    pytest
                '''
            }
        }

        stage('Coverage Report') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    coverage run -m pytest
                    coverage report
                    coverage html
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
