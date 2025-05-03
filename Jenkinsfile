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

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                    # Check if python3-venv is installed
                    if ! python3 -m venv --help > /dev/null 2>&1; then
                        echo "python3-venv is not installed. Please install it first." && exit 1
                    fi
                    # Create a virtual environment
                    python3 -m venv $VENV
                    # Upgrade pip and install dependencies
                    $VENV/bin/pip install --upgrade pip
                    $VENV/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    # Run pytest within the virtual environment
                    $VENV/bin/python -m pytest
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '**/test-*.xml' // Adjust this if your tests generate a specific test report file
            }
        }
    }

    post {
        always {
            // Clean up by removing the virtual environment
            sh 'rm -rf $VENV || true'
        }
    }
}
