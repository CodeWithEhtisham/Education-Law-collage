pipeline {
    agent any

    stages {
        stage('Packages upgrade') {
            steps {
                sh """
                sudo chmod +x ./configurations/gunicorn.sh
                sudo chmod +x ./configurations/nginx.sh
                sudo chmod +x ./configurations/virtual_env.sh
                """
                sh 'sudo apt update && sudo apt install python3-pip nginx curl -y'
            }
        }

        stage('Virtual environment') {
            steps {
                sh './configurations/virtual_env.sh'
            }
        }

        stage('Django migrate') {
            steps {
                sh 'python3.8 ./manage.py makemigrations'
                sh 'python3.8 ./manage.py migrate'
                sh 'python3.8 ./manage.py collectstatic --noinput'
            }
        }

        stage('Gunicorn setup') {
            steps {
                sh './configurations/gunicorn.sh'
                sh 'sudo systemctl status education'
            }
        }

        stage('Nginx setup') {
            steps {
                sh './configurations/nginx.sh'
            }
        }

        stage('Nginx test') {
            steps {
                sh 'echo $(sudo nginx -t)'
                sh 'sudo systemctl enable --now nginx'
                sh 'sudo systemctl restart nginx'
                sh 'sudo systemctl status nginx'
            }
        }
    }
}