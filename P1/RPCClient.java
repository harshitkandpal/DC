package DC.P1;

import java.io.*;
import java.net.*;
import java.util.*;

public class RPCClient {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        // Local Function Call
        long startLocal = System.nanoTime();
        int localSum = a + b;
        long endLocal = System.nanoTime();

        System.out.println("Local Sum: " + localSum);
        System.out.println("Local Time: " + (endLocal - startLocal) + " ns");

        // RPC Call
        Socket socket = new Socket("localhost", 5000);

        BufferedReader input = new BufferedReader(
                new InputStreamReader(socket.getInputStream()));

        PrintWriter output = new PrintWriter(
                socket.getOutputStream(), true);

        long startRPC = System.nanoTime();
        output.println(a + " " + b);
        int rpcSum = Integer.parseInt(input.readLine());
        long endRPC = System.nanoTime();

        System.out.println("RPC Sum: " + rpcSum);
        System.out.println("RPC Time: " + (endRPC - startRPC) + " ns");

        socket.close();
        sc.close();
    }
}