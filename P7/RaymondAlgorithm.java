package DC.P7;

import java.util.Scanner;

public class RaymondAlgorithm {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] holder = new int[n + 1];

        System.out.println("Enter holder for each process:");
        System.out.println("(If process itself has token, enter its own ID)");

        // Input holder structure
        for (int i = 1; i <= n; i++) {
            System.out.print("Holder of Process " + i + ": ");
            holder[i] = sc.nextInt();
        }

        // Requesting process
        System.out.print("Enter process requesting Critical Section: ");
        int requester = sc.nextInt();

        if (requester < 1 || requester > n) {
            System.out.println("Invalid process ID.");
            return;
        }

        System.out.println("\nRequest path:");

        int current = requester;

        // Traverse until token holder is found
        while (current != holder[current]) {
            System.out.println("Process " + current +
                    " sends REQUEST to Process " + holder[current]);

            current = holder[current];
        }

        // Token holder found
        System.out.println("\nProcess " + current +
                " holds the TOKEN.");

        System.out.println("TOKEN is passed to Process " + requester);

        // Update token path
        holder[requester] = requester;

        System.out.println("Process " + requester +
                " enters Critical Section.");

        System.out.println("Process " + requester +
                " exits Critical Section.");

        sc.close();
    }
}