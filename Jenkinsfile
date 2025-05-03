pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Bhargavkulla/retest-jenkins-1.git', branch: 'main'
            }
        }

        stage('Install virtualenv and Set Up Virtual Environment') {
            steps {
                sh '''
                    # Install virtualenv if it's not installed
                    python3 -m pip install --user virtualenv
                    
                    # Create the virtual environment using virtualenv
                    python3 -m virtualenv $VENV
                    
                    # Upgrade pip inside the virtual environment
                    $VENV/bin/pip install --upgrade pip
                    
                    # Install dependencies from requirements.txt
                    $VENV/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    # Run pytest and generate a JUnit XML report
                    $VENV/bin/python -m pytest --junitxml=pytest-report.xml
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '**/pytest-report.xml'  // Look for the generated XML report
            }
        }
    }

    post {
        always {
            // Clean up by removing the virtual environment after the pipeline finishes
            sh 'rm -rf $VENV || true'
        }
    }
}
