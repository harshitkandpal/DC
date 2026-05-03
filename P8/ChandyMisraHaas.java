package DC.P8;

import java.util.Scanner;

public class ChandyMisraHaas {

    static int[][] waitGraph;
    static int n;
    static boolean deadlock = false;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        n = sc.nextInt();

        waitGraph = new int[n][n];

        System.out.println("Enter Wait-For Graph matrix:");
        System.out.println("(Enter 1 if Pi waits for Pj, else 0)");

        // Input graph
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                waitGraph[i][j] = sc.nextInt();
            }
        }

        System.out.print("Enter initiator process (1 to " + n + "): ");
        int initiator = sc.nextInt() - 1;

        boolean[] visited = new boolean[n];

        System.out.println("\nProbe Messages:");
        detectDeadlock(initiator, initiator, visited);

        if (deadlock) {
            System.out.println("\nDeadlock Detected.");
        } else {
            System.out.println("\nNo Deadlock.");
        }

        sc.close();
    }

    static void detectDeadlock(int initiator, int current, boolean[] visited) {

        visited[current] = true;

        for (int next = 0; next < n; next++) {

            if (waitGraph[current][next] == 1) {

                System.out.println("Probe (" +
                        (initiator + 1) + ", " +
                        (current + 1) + ", " +
                        (next + 1) + ")");

                // Cycle found
                if (next == initiator) {
                    deadlock = true;
                    return;
                }

                if (!visited[next]) {
                    detectDeadlock(initiator, next, visited);
                }
            }
        }

        visited[current] = false;
    }
}