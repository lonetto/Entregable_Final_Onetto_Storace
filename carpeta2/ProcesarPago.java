public class ProcesarPago implements Runnable {
    private Pedido pedido;

    public ProcesarPago(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public void run() {
        try {
            System.out.println("Procesando pago para " + pedido);
            // Simulación de procesamiento de pago con un delay
            Thread.sleep(1000);
            System.out.println("Pago procesado para " + pedido);
        } catch (InterruptedException e) {
            // Restaurar el estado de interrupción y manejar la interrupción adecuadamente
            System.out.println("El procesamiento del pago fue interrumpido para " + pedido);
            Thread.currentThread().interrupt(); // Volver a establecer el estado de interrupción del hilo
        }
    }
}



