package DC.P5;

import java.util.Scanner;

public class RingAlgorithm {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] processes = new int[n];

        // Process status
        System.out.println("Enter process status (1 = alive, 0 = dead):");
        for (int i = 0; i < n; i++) {
            System.out.print("Process " + (i + 1) + ": ");
            processes[i] = sc.nextInt();
        }

        // Initiator
        System.out.print("Enter process initiating election: ");
        int initiator = sc.nextInt();

        if (processes[initiator - 1] == 0) {
            System.out.println("Initiator process is dead.");
            return;
        }

        System.out.println("\nElection message passing:");

        int current = initiator;
        int coordinator = initiator;

        do {
            int next = (current % n) + 1;

            // Find next alive process
            while (processes[next - 1] == 0) {
                next = (next % n) + 1;
            }

            System.out.println("Process " + current +
                    " sends election message to Process " + next);

            if (next > coordinator) {
                coordinator = next;
            }

            current = next;

        } while (current != initiator);

        System.out.println("\nProcess " + coordinator +
                " becomes the new Coordinator.");

        sc.close();
    }
}