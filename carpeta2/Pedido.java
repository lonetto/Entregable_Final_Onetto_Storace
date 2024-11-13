public class Pedido implements Comparable<Pedido> {
    private int id;
    private boolean urgente;
    private long ordenLlegada;  // Campo para almacenar el orden de llegada

    private static long contador = 0;  // Contador global para asignar el orden de llegada

    public Pedido(int id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
        this.ordenLlegada = contador++;  // Asignamos un número único a cada pedido en el orden en que es creado
    }

    public int getId() {
        return id;
    }

    public boolean isUrgente() {
        return urgente;
    }

    @Override
    public String toString() {
        return "Pedido{" +
                "id=" + id +
                ", urgente=" + urgente +
                ", ordenLlegada=" + ordenLlegada +
                '}';
    }

    @Override
    public int compareTo(Pedido otroPedido) {
        // Primero, comparar por urgencia
        if (this.urgente && !otroPedido.isUrgente()) {
            return -1; // Si este es urgente y el otro no, darle prioridad a este
        } else if (!this.urgente && otroPedido.isUrgente()) {
            return 1;  // Si el otro es urgente y este no, darle prioridad al otro
        } else {
            // Si ambos son iguales en urgencia, comparar por el orden de llegada (FIFO)
            return Long.compare(this.ordenLlegada, otroPedido.ordenLlegada);
        }
    }
}



