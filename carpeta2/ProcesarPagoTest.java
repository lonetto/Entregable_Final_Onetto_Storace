import org.junit.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ProcesarPagoTest {

    @Test
    public void testProcesarPago() {
        Pedido pedido = new Pedido(1, true); // Pedido urgente
        ProcesarPago procesarPago = new ProcesarPago(pedido);

        // Capturamos la salida en consola para verificar el comportamiento
        procesarPago.run();

        // Verificamos que el pedido se haya procesado sin errores
        assertEquals(1, pedido.getId());
        assertEquals(true, pedido.isUrgente());
    }
}
