pipeline{
    agent any

    stages{
        stage('prepare-env'){
            steps{
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip install -r requirements.txt"
            }
        }
        stage('start-tests'){
            steps{
                sh "python3 pytest --browser chrome"
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