pipeline {
    agent any
    
    environment {
        // Puedes definir variables de entorno aquí si las necesitas
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lonetto/Entregable_Final_Onetto_Storace.git'
            }
        }
        
        stage('Build - Carpeta2') {
            steps {
                dir('carpeta2') {
                    echo 'Compiling Java code in carpeta2...'
                    bat 'javac -cp "C:/ruta/a/junit-platform-console-standalone-1.8.1.jar;." *.java' // Ajusta la ruta del archivo jar de JUnit según tu sistema.
                }
            }
        }
        
        stage('Test - Carpeta1') {
            steps {
                dir('carpeta1') {
                    echo 'Running tests in carpeta1...'
                    bat 'java -jar C:/ruta/a/junit-platform-console-standalone-1.8.1.jar -cp . --select-package carpeta1'
                }
            }
        }
        
        stage('Test - Carpeta2') {
            steps {
                dir('carpeta2') {
                    echo 'Running tests in carpeta2...'
                    bat 'java -jar C:/ruta/a/junit-platform-console-standalone-1.8.1.jar -cp . --select-package carpeta2'
                }
            }
        }
        
        stage('Test - Carpeta3') {
            steps {
                dir('carpeta3') {
                    echo 'Running tests in carpeta3...'
                    bat 'java -jar C:/ruta/a/junit-platform-console-standalone-1.8.1.jar -cp . --select-package carpeta3'
                }
            }
        }
        
        stage('Deploy') {
            when {
                success()
            }
            steps {
                echo 'Deployment stage (aquí agrega los pasos de deployment si los necesitas)...'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'El pipeline ha terminado exitosamente.'
        }
        failure {
            echo 'El pipeline ha fallado.'
            mail to: 'tu-email@example.com',
                 subject: 'Pipeline Failed',
                 body: "El pipeline ha fallado en la ejecución. Verifica Jenkins para más detalles."
        }
    }
}

