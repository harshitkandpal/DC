package DC.P1;

import java.io.*;
import java.net.*;

public class RPCServer {
    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(5000);
        System.out.println("Server waiting...");

        while (true) {
            Socket socket = server.accept();

            BufferedReader input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));

            PrintWriter output = new PrintWriter(
                    socket.getOutputStream(), true);

            String data = input.readLine();
            String[] numbers = data.split(" ");

            int a = Integer.parseInt(numbers[0]);
            int b = Integer.parseInt(numbers[1]);

            System.out.println("Received: " + a + " and " + b);

            int sum = a + b;
            System.out.println("Processed Request: Computed Sum " + sum);
            output.println(sum);

            socket.close();
        }
    }
}