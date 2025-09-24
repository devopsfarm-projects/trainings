node {
    stage('Checkout') {
        sh "echo 'Checking out the source code...'"
    }

    stage('Build') {
        sh 'echo "Building the project... "'
    }

    stage('Test') {
        sh 'echo "Running tests..."'
    }

    stage('Deploy') {
        sh 'echo "Deploying the application..."'
    }

    stage('Cleanup') {
        sh 'echo "Cleaning up..."'
    }
}