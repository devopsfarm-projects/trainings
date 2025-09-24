pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                echo "Checking out the source code..."
            }
        }
        stage("Build"){
            steps {
                echo "Building the project..."
            }
        }

        stage("Test"){
            steps {
                echo "Running tests..."
            }
        }

        stage("Deploy"){
            steps {
                echo "Deploying the application..."
            }
        }

        stage("Cleanup"){
            steps {
                echo "Cleaning up..."
            }
        }
    }
}