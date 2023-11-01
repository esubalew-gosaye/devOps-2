pipeline {
    agent any

    stages {
        stage('GitHub Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/esubalew-gosaye/devOps-2.git']])
            }
        }
        stage("Build Docker Image"){
            steps{
                script{
                   sh 'docker build -t devOps-2/simple-jenk-dj .'
                }
            }
        }
    }
}
