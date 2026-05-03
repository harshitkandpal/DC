package DC.P4;

import java.util.Scanner;

public class BullyAlgorithm {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] processes = new int[n];

        // Input process IDs
        System.out.println("Enter process IDs:");
        for (int i = 0; i < n; i++) {
            processes[i] = sc.nextInt();
        }

        // Current coordinator
        int coordinator = processes[n - 1];

        System.out.println("Current Coordinator: Process " + coordinator);

        // Failed coordinator
        System.out.print("Enter failed coordinator ID: ");
        int failed = sc.nextInt();

        if (failed != coordinator) {
            System.out.println("Entered process is not the current coordinator.");
            return;
        }

        // Initiator process
        System.out.print("Enter process that detects failure: ");
        int initiator = sc.nextInt();

        System.out.println("\nProcess " + initiator + " starts election.");

        int newCoordinator = initiator;

        // Send election messages to higher processes
        for (int i = 0; i < n; i++) {
            if (processes[i] > initiator && processes[i] != failed) {
                System.out.println("Election message sent from Process " +
                        initiator + " to Process " + processes[i]);

                System.out.println("Process " + processes[i] +
                        " responds OK");

                newCoordinator = processes[i];
            }
        }

        System.out.println("\nProcess " + newCoordinator +
                " becomes the new Coordinator.");

        sc.close();
    }
}