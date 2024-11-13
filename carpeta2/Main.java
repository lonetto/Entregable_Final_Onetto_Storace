import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.PriorityBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) {
        // Crear las colas
        PriorityBlockingQueue<Pedido> colaDePedidos = new PriorityBlockingQueue<>(); // Cola de pedidos originales
        BlockingQueue<Pedido> colaDePedidosProcesados = new LinkedBlockingQueue<>(); // Cola de pedidos procesados
        BlockingQueue<Pedido> colaDePedidosEmpaquetados = new LinkedBlockingQueue<>(); // Cola de pedidos empaquetados

        // Crear y agregar pedidos a la cola inicial
        for (int i = 1; i <= 10; i++) {
            Pedido pedido = new Pedido(i, i % 3 == 0); // Pedidos urgentes cada 3 pedidos
            colaDePedidos.put(pedido); // Insertar pedido en la cola
        }

        // Crear pools de hilos
        ExecutorService poolProcesarPago = Executors.newFixedThreadPool(3); // 3 hilos para procesamiento de pago
        ExecutorService poolEmpaquetarPedido = Executors.newFixedThreadPool(2); // 2 hilos para empaquetar pedidos
        ExecutorService poolEnviarPedido = Executors.newFixedThreadPool(2); // 2 hilos para enviar pedidos

        // Procesar los pedidos en orden de prioridad (primera etapa: procesar pago)
        for (int i = 0; i < 3; i++) { // 3 hilos asignados a esta tarea
            poolProcesarPago.submit(() -> {
                while (true) {
                    try {
                        Pedido pedido = colaDePedidos.take(); // Tomar el pedido de mayor prioridad
                        ProcesarPago procesarPago = new ProcesarPago(pedido);
                        procesarPago.run();
                        colaDePedidosProcesados.put(pedido); // Agregar a la cola de procesados
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }

        // Empaquetar los pedidos procesados (segunda etapa)
        for (int i = 0; i < 2; i++) { // 2 hilos asignados a esta tarea
            poolEmpaquetarPedido.submit(() -> {
                while (true) {
                    try {
                        Pedido pedido = colaDePedidosProcesados.take(); // Tomar el siguiente pedido procesado
                        EmpaquetarPedido empaquetarPedido = new EmpaquetarPedido(pedido);
                        empaquetarPedido.run();
                        colaDePedidosEmpaquetados.put(pedido); // Agregar a la cola de empaquetados
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }

        // Enviar los pedidos empaquetados (tercera etapa)
        for (int i = 0; i < 2; i++) { // 2 hilos asignados a esta tarea
            poolEnviarPedido.submit(() -> {
                while (true) {
                    try {
                        Pedido pedido = colaDePedidosEmpaquetados.take(); // Tomar el siguiente pedido empaquetado
                        EnviarPedido enviarPedido = new EnviarPedido(pedido);
                        enviarPedido.run();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }

        // Cerrar los pools de hilos de manera ordenada (con awaitTermination)
        poolProcesarPago.shutdown();
        poolEmpaquetarPedido.shutdown();
        poolEnviarPedido.shutdown();

        try {
            // Esperamos a que todos los hilos terminen sus tareas
            if (!poolProcesarPago.awaitTermination(60, TimeUnit.SECONDS)) {
                poolProcesarPago.shutdownNow();
            }
            if (!poolEmpaquetarPedido.awaitTermination(60, TimeUnit.SECONDS)) {
                poolEmpaquetarPedido.shutdownNow();
            }
            if (!poolEnviarPedido.awaitTermination(60, TimeUnit.SECONDS)) {
                poolEnviarPedido.shutdownNow();
            }
        } catch (InterruptedException e) {
            poolProcesarPago.shutdownNow();
            poolEmpaquetarPedido.shutdownNow();
            poolEnviarPedido.shutdownNow();
        }
    }
}

