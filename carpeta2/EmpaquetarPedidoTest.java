import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class EmpaquetarPedidoTest {

    @Test
    public void testEmpaquetarPedido() {
        Pedido pedido = new Pedido(2, false); // Pedido normal
        EmpaquetarPedido empaquetarPedido = new EmpaquetarPedido(pedido);

        // Simulamos la ejecución del empaquetado
        empaquetarPedido.run();

        // Verificamos que el pedido fue correctamente empaquetado
        assertEquals(2, pedido.getId());
        assertEquals(false, pedido.isUrgente());
    }
}
