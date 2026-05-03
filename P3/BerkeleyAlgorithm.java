package DC.P3;

import java.util.Scanner;

public class BerkeleyAlgorithm {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();

        int[] clocks = new int[n];
        int sum = 0;

        // Input clock times
        for (int i = 0; i < n; i++) {
            System.out.print("Enter time for Node " + (i + 1) + ": ");
            clocks[i] = sc.nextInt();
            sum += clocks[i];
        }

        // Master computes average
        int average = sum / n;

        System.out.println("\nCoordinator computes average time: " + average);

        // Synchronization
        System.out.println("\nClock Adjustments:");
        for (int i = 0; i < n; i++) {
            int adjustment = average - clocks[i];
            System.out.println(
                    "Node " + (i + 1) +
                            " adjusts by " + adjustment +
                            " units -> New Time: " + (clocks[i] + adjustment));
        }

        sc.close();
    }
}