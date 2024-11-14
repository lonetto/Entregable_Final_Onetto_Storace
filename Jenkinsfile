pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio desde GitHub
                git url: 'https://github.com/lonetto/Entregable_Final_Onetto_Storace.git', branch: 'main'
            }
        }
        stage('Build - Carpeta2') {
            steps {
                dir('carpeta2') {
                    // Compilar código Java en carpeta2
                    echo 'Compiling Java code in carpeta2...'
                    bat 'javac *.java'
                }
            }
        }
        stage('Test - Carpeta1') {
            steps {
                dir('carpeta1') {
                    // Ejecutar pruebas en Python para carpeta1
                    echo 'Running Python tests in carpeta1...'
                    bat 'python -m unittest test_general.py'
                }
            }
        }
        stage('Test - Carpeta2') {
            steps {
                dir('carpeta2') {
                    // Ejecutar pruebas en Java para carpeta2
                    echo 'Running Java tests in carpeta2...'
                    bat 'java -cp . org.junit.runner.JUnitCore EmpaquetarPedidoTest ProcesarPagoTest EnviarPedidoTest'
                }
            }
        }
        stage('Test - Carpeta3') {
            steps {
                dir('carpeta3') {
                    // Ejecutar pruebas en Python para carpeta3
                    echo 'Running Python tests in carpeta3...'
                    bat 'python -m unittest test_fluent_api.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                // Despliegue de la aplicación o scripts necesarios
                echo 'Deploying application...'
                // Comandos específicos de despliegue (si tienes alguno)
            }
        }
    }
    post {
        always {
            // Notificación al final de la ejecución
            mail to: 'tu_correo@example.com',
                 subject: "Resultado del Pipeline: ${currentBuild.currentResult}",
                 body: "Revisa el estado del pipeline en Jenkins."
        }
        success {
            echo 'Pipeline ejecutado exitosamente.'
        }
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}
