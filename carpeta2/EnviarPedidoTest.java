import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class EnviarPedidoTest {

    @Test
    public void testEnviarPedido() {
        Pedido pedido = new Pedido(3, false); // Pedido normal
        EnviarPedido enviarPedido = new EnviarPedido(pedido);

        // Simulamos la ejecución del envío
        enviarPedido.run();

        // Verificamos que el pedido fue correctamente enviado
        assertEquals(3, pedido.getId());
        assertEquals(false, pedido.isUrgente());
    }
}
