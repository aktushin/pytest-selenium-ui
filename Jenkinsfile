pipeline{
    agent any

    stages{
        stage('prepare-and-start-tests'){
            steps{
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip install -r requirements.txt"
                sh "pytest --browser chrome"
            }
        }
    }
}
post{
    always{
        allure([
            reportBuildPolicy: 'ALWAYS',
            results: [[path: 'allure-results']]
        ])
    }
}