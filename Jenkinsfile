pipeline{
    agent any

    stages{
        stage('ui-tests'){
            parallel{
                stage('chrome-last'){
                    agent{
                        node{
                            label "docker"
                            customWorkspace "workspace/chrome-last"
                            }
                        }
                steps{
                    script{
                        sh "docker build -t chrome-last --target chrome_last ."
                        sh "docker run chrome-last --rm --shm-size='4g' --browser chrome --headless -n 2 --alluredir=allure-results"
                    }
                }
                post{
                    always{
                        allure([
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: '/allure-results']]
                        ])
                    }
                }
            }
            stage('firefox-last'){
                    agent{
                        node{
                            label "docker"
                            customWorkspace "workspace/firefox-last"
                            }
                        }
                steps{
                    script{
                        sh "docker build -t firefox-last --target firefox_last ."
                        sh "docker run firefox-last --rm --shm-size='4g' --browser firefox --headless -n 2 --alluredir=allure-results"
                    }
                }
                post{
                    always{
                        allure([
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: '/allure-results']]
                        ])
                    }
                }
            }
            }
        }
    }
}
