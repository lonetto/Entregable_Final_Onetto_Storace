import java.util.concurrent.*;

public class MainCarga {
    public static void main(String[] args) {
        // Iniciar el timer
        long startTime = System.currentTimeMillis();

        // Crear las colas
        PriorityBlockingQueue<Pedido> colaDePedidos = new PriorityBlockingQueue<>();
        BlockingQueue<Pedido> colaDePedidosProcesados = new LinkedBlockingQueue<>();
        BlockingQueue<Pedido> colaDePedidosEmpaquetados = new LinkedBlockingQueue<>();

        // Crear y agregar 1000000 pedidos a la cola inicial
        for (int i = 1; i <= 100; i++) {
            Pedido pedido = new Pedido(i, i % 3 == 0); // Pedidos urgentes cada 3 pedidos
            colaDePedidos.put(pedido); // Insertar pedido en la cola
        }

        // Crear pools de hilos
        ExecutorService poolProcesarPago = Executors.newFixedThreadPool(10);
        ExecutorService poolEmpaquetarPedido = Executors.newFixedThreadPool(8);
        ExecutorService poolEnviarPedido = Executors.newFixedThreadPool(8);

        // Procesar los pedidos (primera etapa)
        for (int i = 0; i < 5; i++) {
            poolProcesarPago.submit(() -> {
                try {
                    while (!Thread.currentThread().isInterrupted()) {
                        Pedido pedido = colaDePedidos.take();
                        ProcesarPago procesarPago = new ProcesarPago(pedido);
                        procesarPago.run();
                        colaDePedidosProcesados.put(pedido);
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt(); // Restaurar el estado de interrupción
                }
            });
        }

        // Empaquetar los pedidos procesados (segunda etapa)
        for (int i = 0; i < 4; i++) {
            poolEmpaquetarPedido.submit(() -> {
                try {
                    while (!Thread.currentThread().isInterrupted()) {
                        Pedido pedido = colaDePedidosProcesados.take();
                        EmpaquetarPedido empaquetarPedido = new EmpaquetarPedido(pedido);
                        empaquetarPedido.run();
                        colaDePedidosEmpaquetados.put(pedido);
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt(); // Restaurar el estado de interrupción
                }
            });
        }

        // Enviar los pedidos empaquetados (tercera etapa)
        for (int i = 0; i < 3; i++) {
            poolEnviarPedido.submit(() -> {
                try {
                    while (!Thread.currentThread().isInterrupted()) {
                        Pedido pedido = colaDePedidosEmpaquetados.take();
                        EnviarPedido enviarPedido = new EnviarPedido(pedido);
                        enviarPedido.run();
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt(); // Restaurar el estado de interrupción
                }
            });
        }

        // Cerrar los pools de hilos de manera ordenada
        poolProcesarPago.shutdown();
        poolEmpaquetarPedido.shutdown();
        poolEnviarPedido.shutdown();

        try {
            if (!poolProcesarPago.awaitTermination(60, TimeUnit.SECONDS)) {
                System.out.println("Termino tiempo para el pool procesar pago");
                poolProcesarPago.shutdownNow();
            }
            if (!poolEmpaquetarPedido.awaitTermination(60, TimeUnit.SECONDS)) {
                System.out.println("Termino el tiempo para el pool empaquetar pedido");
                poolEmpaquetarPedido.shutdownNow();
            }
            if (!poolEnviarPedido.awaitTermination(60, TimeUnit.SECONDS)) {
                System.out.println("Termino el tiempo para el pool enviar pedido");
                poolEnviarPedido.shutdownNow();
            }
        } catch (InterruptedException e) {
            poolProcesarPago.shutdownNow();
            poolEmpaquetarPedido.shutdownNow();
            poolEnviarPedido.shutdownNow();
        }

        // Calcular y mostrar el tiempo total transcurrido
        long endTime = System.currentTimeMillis();
        long totalTime = (endTime - startTime) / 1000; // Convertir a segundos
        System.out.println("Tiempo total de procesamiento: " + totalTime + " segundos.");
    }
}


