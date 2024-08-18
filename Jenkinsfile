pipeline {
    agent any
    
    environment {
        // Specify the Python version and the virtual environment directory
        PYTHON_VERSION = '3.9'
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/5P4RK3R/Blink.git'
            }
        }
        
        stage('Set Up Python Environment') {
            steps {
                // Install Python if necessary and create a virtual environment
                sh '''
                if ! command -v python$PYTHON_VERSION &> /dev/null
                then
                    echo "Python $PYTHON_VERSION not found, installing..."
                    brew install python@$PYTHON_VERSION
                fi
                
                python$PYTHON_VERSION -m venv $VENV_DIR
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Activate the virtual environment and install dependencies
                sh '''
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run any tests you have defined
                sh '''
                source $VENV_DIR/bin/activate
                pytest
                '''
            }
        }
        
        stage('Deploy Streamlit App') {
            steps {
                // Start the Streamlit app
                sh '''
                source $VENV_DIR/bin/activate
                nohup streamlit run app.py &
                '''
            }
        }
    }
    
    post {
        always {
            // Clean up the workspace after the build is complete
            cleanWs()
        }
    }
}
