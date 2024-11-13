public class EnviarPedido implements Runnable {
    private Pedido pedido;

    public EnviarPedido(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public void run() {
        try {
            System.out.println("Enviando pedido " + pedido);
            // Simulación del envío con un delay
            Thread.sleep(2000);
            System.out.println("Pedido enviado " + pedido);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
