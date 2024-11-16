pipeline {
    agent any
    
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
                    bat 'javac -cp "C:/Users/lucas/OneDrive/Escritorio/JUnit/junit-platform-console-standalone-1.8.1.jar;." *.java'
                }
            }
        }
        
        stage('Test - Carpeta1') {
            steps {
                dir('carpeta1') {
                    echo 'Running tests in carpeta1...'
                    bat 'java -jar C:/Users/lucas/OneDrive/Escritorio/JUnit/junit-platform-console-standalone-1.8.1.jar -cp . --select-package carpeta1'
                }
            }
        }
        
        stage('Test - Carpeta2') {
            steps {
                dir('carpeta2') {
                    echo 'Running tests in carpeta2...'
                    bat 'java -jar C:/Users/lucas/OneDrive/Escritorio/JUnit/junit-platform-console-standalone-1.8.1.jar -cp . --select-package carpeta2'
                }
            }
        }
        
        stage('Test - Carpeta3') {
            steps {
                dir('carpeta3') {
                    echo 'Running tests in carpeta3...'
                    bat 'java -jar C:/Users/lucas/OneDrive/Escritorio/JUnit/junit-platform-console-standalone-1.8.1.jar -cp . --select-package carpeta3'
                }
            }
        }
        
        stage('Deploy') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                // Aquí es donde se deberían agregar los pasos de despliegue en el futuro, 
                // como copiar artefactos a un servidor, hacer un push a un entorno de nube, etc.
                echo 'Deployment stage (aquí agrega los pasos de deployment si se necesita)...'
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
            mail to: 'progavanzadalg@gmail.com',
                 subject: 'Pipeline Failed',
                 body: "El pipeline ha fallado en la ejecución. Verifica Jenkins para más detalles."
        }
    }
}




