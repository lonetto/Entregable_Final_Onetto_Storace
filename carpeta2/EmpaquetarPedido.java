public class EmpaquetarPedido implements Runnable {
    private Pedido pedido;

    public EmpaquetarPedido(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public void run() {
        try {
            System.out.println("Empaquetando pedido " + pedido);
            // Simulación de empaquetado con un delay
            Thread.sleep(1500);
            System.out.println("Pedido empaquetado " + pedido);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}


