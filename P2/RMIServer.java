package DC.P2;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            // Start RMI Registry on port 1099
            LocateRegistry.createRegistry(1099);

            // Create remote object
            CalculatorImpl calc = new CalculatorImpl();

            // Bind object with name "CalculatorService"
            Naming.rebind("rmi://localhost/CalculatorService", calc);

            System.out.println("RMI Server is running successfully...");
            System.out.println("Calculator service is ready.");

        } catch (Exception e) {
            System.out.println("Server Exception: " + e);
        }
    }
}