pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the Git repository
                git 'https://github.com/nidan2110/hacker_rank_automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the tests
                bat 'pytest --html=reports/report.html --self-contained-html'
            }
        }

        stage('Archive Reports') {
            steps {
                // Archive HTML reports
                archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false,
                    keepAll: true
                ])
            }
        }
    }

    post {
        always {
            // Publish JUnit test results if you have XML reports
            junit '**/test-results/*.xml'
        }
    }
}
